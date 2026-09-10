"""Prepare native realizations and their material effects, without applying them."""

from dataclasses import replace
from pathlib import Path, PurePosixPath
import re
import tomllib

import yaml

from .catalog import Catalog, File, KoraError, digest, safe_relative
from .install import _file_bytes


def _profile_name(target: str, profile: str | None) -> str | None:
    if profile is None:
        return None
    if target != "hermes":
        raise KoraError("--profile solo está disponible para skills de Hermes")
    profile = profile.strip().lower()
    if profile == "default":
        raise KoraError("El perfil default es la raíz de Hermes; omitir --profile")
    # Matches named profile IDs in the installed Hermes, without importing it.
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", profile) or profile in {
        "hermes", "test", "tmp", "root", "sudo"
    }:
        raise KoraError(f"Nombre de perfil Hermes inválido: {profile!r}")
    return profile


def _bundle_key(target: str, identifier: str, profile: str | None = None) -> str:
    return f"hermes@profile:{profile}:{identifier}" if profile is not None else f"{target}:{identifier}"


def _selection(catalog: Catalog, target: str, identifiers, profile):
    selected = ([catalog.get(identifier) for identifier in identifiers] if identifiers else
                [catalog.get(p.id) for p in catalog.products.values() if p.kind != "knowledge" and target in p.targets
                 and (profile is None or p.kind == "skill")])
    if profile is not None and any(product.kind != "skill" for product in selected):
        raise KoraError("--profile solo admite productos skill; no cambia el perfil de un agente")
    return [(product, profile) for product in selected]


def _build_instances_in_phase(catalog: Catalog, target: str, instances) -> dict[str, dict[str, File]]:
    if target == "codex":
        from .render_codex import render
    elif target == "hermes":
        from .render_hermes import render
    else:
        raise KoraError(f"Destino desconocido: {target}")
    instances = [(catalog.capture(product), profile) for product, profile in instances]
    for product, profile in instances:
        if profile is not None and product.kind != "skill":
            raise KoraError(f"La instancia del perfil {profile} requiere una skill activa: {product.id}")
    bundles = {}
    for product, profile in instances:
        files = render(catalog, product)
        pins = {edge["target"]: edge["requested_revision"]
                for edge in catalog.explain(product, target)["edges"]
                if edge["status"] == "available" and edge["requested_revision"]}
        files = {path: replace(file, source={**file.source,
                                             "pinned_revision": pins.get(file.source["id"])})
                 if file.source else file for path, file in files.items()}
        if profile is not None:
            prefix = ".hermes/skills/"
            if any(not path.startswith(prefix) for path in files):
                raise KoraError(f"La realización de skill invade otro ámbito: {product.id}")
            files = {f".hermes/profiles/{profile}/skills/{path[len(prefix):]}": file
                     for path, file in files.items()}
        bundles[_bundle_key(target, product.id, profile)] = files
    # Check physical collisions before any output directory or runtime is touched.
    flat = {}
    for files in bundles.values():
        for relative, file in files.items():
            safe_relative(relative)
            if relative in flat and flat[relative] != file:
                raise KoraError(f"Colisión de realización en {target}: {relative}")
            flat[relative] = file
    return bundles


def _build_instances(catalog: Catalog, target: str, instances):
    owns_phase = not catalog.in_phase
    with catalog.phase():
        bundles = _build_instances_in_phase(catalog, target, instances)
        if owns_phase:
            catalog.revalidate()
        return bundles


def build(catalog: Catalog, target: str, identifiers=(), *, profile=None) -> dict[str, dict[str, File]]:
    profile = _profile_name(target, profile)
    return _build_instances(catalog, target, _selection(catalog, target, identifiers, profile))



def instance_key(bundle):
    for target in ('codex', 'hermes'):
        if bundle.startswith(target + ':'):
            return target, bundle[len(target) + 1:], None
    if bundle.startswith('hermes@profile:'):
        profile, separator, identifier = bundle[len('hermes@profile:'):].partition(':')
        if not separator or not identifier:
            raise KoraError(f'Recibo de instancia Hermes inválido: {bundle}')
        return 'hermes', identifier, _profile_name('hermes', profile)
    return None


def _physical(info):
    return {key: info[key] for key in ('sha256', 'mode')} if info is not None else None


def _description(file):
    result = {'sha256': digest(file.data), 'mode': file.mode}
    if file.source is not None:
        result['source'] = file.source
    return result


def _layout(path, target):
    if target == 'codex':
        return 'codex'
    match = re.match(r'^(\.hermes/profiles/[^/]+)/', path)
    return match.group(1) if match else '.hermes'


def _owned_file(installer, relative, expected, *, required=True):
    try:
        path = installer._path(relative)
        current = installer._current(relative)
        if current is None:
            raise KoraError(f'Archivo ausente: {relative}')
        file = File(_file_bytes(path), current['mode'], expected.get('source'))
    except (OSError, KoraError) as error:
        if required:
            raise KoraError(f'Archivo propio no disponible para preparar: {relative}') from error
        return None
    if _physical(_description(file)) != _physical(expected):
        if required:
            raise KoraError(f'Se detectó cambio local; conservar y reconciliar: {relative}')
        return None
    return file


def _legacy_sources(catalog, installer, bundle, members, target):
    """Recover old receipt origins from intact native envelopes, then bounded declarations."""
    sources = {}
    for path, info in members.items():
        if isinstance(info.get('source'), dict) and isinstance(info['source'].get('id'), str):
            sources[path] = info['source']
    native_skill = re.compile(r'^(?:\.agents/skills/[^/]+|\.hermes/(?:profiles/[^/]+/)?skills/[^/]+)/SKILL\.md$')
    for path, info in members.items():
        if path in sources or not native_skill.fullmatch(path):
            continue
        file = _owned_file(installer, path, info, required=False)
        if file is None:
            continue
        try:
            text = file.data.decode('utf-8')
            header = yaml.safe_load(text.split('---', 2)[1])
            identifier = (header.get('metadata') or {}).get('kora_id')
            if not identifier:
                found = re.findall(r'^## Recursos locales KORA\r?\n\r?\nIdentidad: `([^`\r\n]+)`\.', text, re.MULTILINE)
                identifier = found[-1] if found else None
            if not isinstance(identifier, str) or not re.fullmatch(r'urn:[A-Za-z0-9:._-]+', identifier):
                continue
            current = catalog._lookup(identifier)
            origin = {'id': current.id, 'kind': current.kind, 'name': header['name'],
                      'fingerprint': None, 'revision': None, 'pinned_revision': None}
        except (KoraError, ValueError, TypeError, AttributeError, KeyError, IndexError, yaml.YAMLError):
            continue
        prefix = path.removesuffix('SKILL.md')
        for relative in members:
            if relative.startswith(prefix):
                sources.setdefault(relative, origin)
        if target == 'codex' and origin['kind'] == 'agent':
            role = f".codex/agents/{origin['name']}.toml"
            if role in members:
                sources.setdefault(role, origin)
    parsed = instance_key(bundle)
    try:
        root = catalog._lookup(parsed[1])
    except KoraError:
        return sources
    pending, seen = [root], set()
    # This fallback establishes relevance for missing/edited old native files.
    # It cannot authorize their replacement; Installer still checks exact bytes.
    while pending:
        item = pending.pop()
        if item.id in seen or item.kind == 'knowledge':
            continue
        seen.add(item.id)
        origin = {'id': item.id, 'kind': item.kind, 'name': item.name,
                  'fingerprint': None, 'revision': item.revision, 'pinned_revision': None}
        if target == 'codex':
            prefixes = [f'.agents/skills/{item.name}/']
            exact = [f'.codex/agents/{item.name}.toml'] if item.kind == 'agent' else []
        else:
            base = f'.hermes/profiles/{parsed[2]}' if parsed[2] else (
                f'.hermes/profiles/{root.name}' if root.kind == 'agent' else '.hermes')
            prefixes = [f'{base}/skills/{item.name}/'] if item.kind == 'skill' else [f'{base}/resources/']
            exact = [f'{base}/SOUL.md', f'{base}/distribution.yaml'] if item.kind == 'agent' else []
        for path in members:
            if path in exact or any(path.startswith(prefix) for prefix in prefixes):
                sources.setdefault(path, origin)
        for need in item.needs:
            if need.kind in ('knowledge', 'capability') or need.target not in (None, target):
                continue
            try:
                dependency = catalog._lookup(need.id)
                if dependency.kind != 'knowledge':
                    pending.append(dependency)
            except KoraError:
                continue
    return sources


def installation_effects(catalog, target, identifiers, installer, profile=None):
    """Build selected definitions and patch only their attributable managed copies."""
    installed = installer.receipts()
    instances = _selection(catalog, target, identifiers, profile)
    if not identifiers:
        selected_keys = {_bundle_key(target, item.id, place) for item, place in instances}
        for key in installed:
            parsed = instance_key(key)
            if parsed and parsed[0] == target and key not in selected_keys:
                if profile is None or parsed[2] == profile:
                    instances.append((catalog.get(parsed[1]), parsed[2]))
    bundles = _build_instances(catalog, target, instances)
    material = {file.source['id'] for files in bundles.values() for file in files.values() if file.source}
    material_revisions = {file.source['id']: file.source.get('revision')
                          for files in bundles.values() for file in files.values() if file.source}
    def material_product(identifier):
        revision = material_revisions[identifier]
        return catalog.at_revision(identifier, revision) if revision else catalog.get(identifier)
    # A registered instance of an already selected dependency is itself in scope.
    for key in installed:
        parsed = instance_key(key)
        if (parsed and parsed[0] == target and key not in bundles and parsed[1] in material
                and (profile is None or parsed[2] == profile)):
            bundles.update(_build_instances(catalog, target, [(material_product(parsed[1]), parsed[2])]))
    canonical = {}
    patches, conflicts, reasons = {}, [], []
    for key, previous in installed.items():
        parsed = instance_key(key)
        if not parsed or parsed[0] != target or key in bundles or (profile is not None and parsed[2] != profile):
            continue
        sources = _legacy_sources(catalog, installer, key, previous, target)
        grouped = {}
        for path, source in sources.items():
            if source['id'] in material:
                grouped.setdefault((source['id'], _layout(path, target)), {})[path] = source
        patch = {}
        for (identifier, layout), owned in grouped.items():
            if identifier not in canonical:
                canonical[identifier] = next(iter(_build_instances(
                    catalog, target, [(material_product(identifier), None)]).values()))
            wanted = canonical[identifier]
            own_sources = [file.source for file in wanted.values() if file.source and file.source['id'] == identifier]
            if not own_sources:
                continue
            source = own_sources[0]
            old_names = {item['name'] for item in owned.values()}
            if old_names != {source['name']}:
                conflicts.append({'bundle': key, 'source': identifier,
                                  'error': 'Cambió el nombre nativo; actualiza explícitamente sus consumidores para conservar sus instrucciones'})
                continue
            rebased = {}
            for path, file in wanted.items():
                relative = (layout + path[len('.hermes'):] if target == 'hermes' else path)
                previous_source = sources.get(relative)
                if previous_source and previous_source['id'] != file.source['id']:
                    conflicts.append({'bundle': key, 'path': relative, 'error': 'El path pertenece a otra identidad nativa'})
                    continue
                pin = previous_source.get('pinned_revision') if previous_source else None
                if pin and pin != file.source.get('revision'):
                    conflicts.append({'bundle': key, 'path': relative, 'source': identifier,
                                      'error': f'Revisión fijada incompatible: {pin}'})
                    continue
                if pin:
                    file = replace(file, source={**file.source, 'pinned_revision': pin})
                rebased[relative] = file
            own_wanted = {path for path, file in rebased.items() if file.source['id'] == identifier}
            for path in set(owned) - own_wanted:
                patch[path] = None
            for path, file in rebased.items():
                old = previous.get(path)
                description = _description(file)
                # Do not migrate an unrelated legacy receipt for unchanged bytes.
                if old is None or _physical(old) != _physical(description) or (
                        old.get('source') is not None and old != description):
                    patch[path] = file
        if not patch:
            continue
        try:
            catalog.require_available(parsed[1], target)
        except KoraError as error:
            conflicts.append({'bundle': key, 'error': str(error)})
            continue
        # Hermes owns a native list of profile files. Update that list from its
        # installed metadata, preserving any pending edits of the source owner.
        manifests = [path for path in previous if path.endswith('/distribution.yaml')]
        for manifest_path in manifests:
            base = manifest_path.removesuffix('/distribution.yaml')
            old_paths = {p for p in previous if p.startswith(base + '/')}
            new_paths = (old_paths - {p for p, f in patch.items() if f is None}) | {
                p for p, f in patch.items() if f is not None and p.startswith(base + '/')}
            if old_paths == new_paths:
                continue
            try:
                native = _owned_file(installer, manifest_path, previous[manifest_path])
                manifest = yaml.safe_load(native.data)
                if not isinstance(manifest, dict) or not isinstance(manifest.get('distribution_owned'), list):
                    raise KoraError(f'Manifiesto nativo no reconocible: {manifest_path}')
                manifest['distribution_owned'] = sorted(p[len(base) + 1:] for p in new_paths)
                patch[manifest_path] = File(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False).encode(),
                                            native.mode, native.source)
            except (KoraError, yaml.YAMLError) as error:
                conflicts.append({'bundle': key, 'path': manifest_path, 'error': str(error)})
        patches[key] = patch
        reasons.append({'bundle': key, 'reason': 'shared_native_files', 'paths': sorted(patch)})
    # Old co-owners of a physical path must receive the same ownership change,
    # even if their current source no longer declares that former dependency.
    physical = {path: file for files in bundles.values() for path, file in files.items()}
    physical.update({path: file for files in patches.values() for path, file in files.items() if file is not None})
    for key, previous in installed.items():
        parsed = instance_key(key)
        if not parsed or parsed[0] != target or key in bundles or (profile is not None and parsed[2] != profile):
            continue
        origins = None
        for path in previous.keys() & physical.keys():
            file = physical[path]
            if _physical(previous[path]) == _physical(_description(file)):
                continue
            try:
                catalog.require_available(parsed[1], target)
                if origins is None:
                    origins = _legacy_sources(catalog, installer, key, previous, target)
                old_source = origins.get(path) or {}
                if old_source.get('id') is None:
                    raise KoraError(f'No se pudo atribuir la identidad del path compartido: {path}')
                if old_source['id'] != file.source['id']:
                    raise KoraError(f'El path compartido pertenece a otra identidad: {path}')
                pin = old_source.get('pinned_revision')
                if pin and pin != file.source.get('revision'):
                    raise KoraError(f'Revisión fijada incompatible: {pin}')
                if pin:
                    file = replace(file, source={**file.source, 'pinned_revision': pin})
                patches.setdefault(key, {})[path] = file
            except KoraError as error:
                conflicts.append({'bundle': key, 'path': path, 'error': str(error)})
    return {'bundles': bundles, 'patches': patches, 'conflicts': conflicts, 'reasons': reasons}

def compare_source(catalog, installer, status, *, target=None, identifiers=(), profile=None):
    rows = []
    selected = set(identifiers)
    for identifier in list(selected):
        try:
            selected.add(catalog._lookup(identifier).id)
        except KoraError:
            pass
    for bundle, previous in installer.receipts().items():
        parsed = instance_key(bundle)
        if not parsed:
            continue
        runtime, identifier, place = parsed
        installed_profile = place
        if runtime == 'hermes' and installed_profile is None:
            # An agent bundle owns a profile without using the separate
            # hermes@profile key reserved for explicit skill instances. Keep
            # that physical context even after its source disappeared.
            profiles = {match.group(1) for path in previous
                        if (match := re.match(r'^\.hermes/profiles/([^/]+)/', path))}
            if len(profiles) == 1:
                installed_profile = next(iter(profiles))
        if (target and runtime != target) or (selected and identifier not in selected) or (profile and installed_profile != profile):
            continue
        row = {'bundle': bundle, 'id': identifier, 'target': runtime, 'profile': installed_profile,
               'native_changes': [change for change in status['changes'] if change['path'] in previous],
               'load_evidence': 'not_observed', 'dependency_state': 'not_checked'}
        availability = catalog.availability(identifier)
        if availability in ('absent', 'retired'):
            row['source_state'] = availability
            rows.append(row)
            continue
        try:
            product = catalog.require_available(identifier, runtime)
            fingerprint = product.fingerprint()
            desired = next(iter(build(catalog, runtime, [identifier], profile=place).values()))
            own = {path: file for path, file in desired.items() if file.source and file.source['id'] == identifier}
            previous_fingerprints = {info['source'].get('fingerprint') for info in previous.values()
                                     if isinstance(info.get('source'), dict) and info['source'].get('id') == identifier}
            changed = (bool(previous_fingerprints) and previous_fingerprints != {fingerprint}) or any(
                _physical(previous.get(path)) != _physical(_description(file)) for path, file in own.items())
            dependencies = {path: file for path, file in desired.items() if path not in own}
            stale_dependencies = any(_physical(previous.get(path)) != _physical(_description(file))
                                     for path, file in dependencies.items()) or bool(previous.keys() - desired.keys())
            row.update(source_state='changed' if changed else 'current', source_fingerprint=fingerprint,
                       dependency_state='changed' if stale_dependencies else 'current',
                       source_changes=[path for path, file in desired.items()
                                       if _physical(previous.get(path)) != _physical(_description(file))],
                       obsolete_paths=sorted(previous.keys() - desired.keys()))
        except (KoraError, ValueError, OSError) as error:
            row.update(source_state='unrealizable', dependency_state='unavailable', error=str(error))
        rows.append(row)
    return rows
