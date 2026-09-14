"""Closed source/summary error vocabulary shared by adapter and monitor.

Leaf module: no product imports, so both the low-level Google adapter and the
monitoring layer can share one catalog without layering cycles. Every member
is a domain literal raised on the synchronize path or a bridge failure name;
never runtime text, bodies, credentials or exception strings. Extend
deliberately when a new literal code is added on that path. Unknown shapes
fall back to a fixed generic per layer.
"""
BRIDGE_ERRORS = frozenset({'invalid_request', 'helper_busy', 'inactive_parent', 'provider_mismatch',
    'helper_monitor_unavailable', 'helper_cleanup_pending', 'validation_timeout', 'evaluation_not_active', 'evaluation_cancelled', 'helper_failed', 'evaluation_unavailable', 'unauthorized',
    'bridge_timeout_error', 'bridge_attribute_error', 'bridge_type_error', 'bridge_os_error',
    'bridge_value_error', 'bridge_internal_error', 'helper_turn_failed',
    'helper_incomplete_result', 'helper_invalid_result', 'helper_write_denied'})

# Curated 2026-09-14 from the _require literal sites, the explicit assignments
# on the synchronize path and the direct SourceError raises in google_sources
# (_get/_gmail_object/_read_selective_message: invalid_json,
# invalid_raw_message, mime_text_decode_degraded, evaluation_unavailable).
# Every member is a domain literal, never runtime text.
SYNC_ERRORS = frozenset({
    'concrete_calendar_required', 'credential_account_mismatch', 'cycle_id_reused',
    'cycle_in_progress', 'cycle_not_active', 'degradation_reason_required',
    'evaluation_unavailable', 'evaluator_unavailable', 'event_revision_missing', 'event_too_large',
    'explicit_account_required', 'explicit_coverage_scope_required',
    'explicit_since_scope_required', 'external_provider_required',
    'final_cursor_missing', 'final_cursor_required', 'full_or_rebuild_required',
    'gmail_calendar_mismatch', 'gmail_profile_mismatch', 'history_message_id_missing',
    'invalid_cycle', 'invalid_evaluation', 'invalid_event', 'invalid_event_list',
    'invalid_external_object', 'invalid_external_status', 'invalid_history',
    'invalid_http_response', 'invalid_json', 'invalid_message_list', 'invalid_mime_type',
    'invalid_next_page_token', 'invalid_page', 'invalid_page_token',
    'invalid_partition', 'invalid_priority_page_state', 'invalid_priority_strategy',
    'invalid_priority_terms', 'invalid_raw_message', 'invalid_response_shape', 'invalid_scope_digest',
    'invalid_source_content', 'invalid_source_limit', 'invalid_source_url',
    'message_identity_or_raw_missing', 'message_metadata_missing',
    'message_text_too_large', 'message_too_large', 'mime_parse_degraded',
    'mime_text_decode_degraded',
    'page_id_reused', 'page_token_cycle', 'priority_requires_selective_scope',
    'priority_strategy_changed_active_cycle', 'priority_terms_changed_active_cycle',
    'projection_recovery_required', 'response_too_large', 'revision_content_conflict',
    'source_config_required', 'source_hash_mismatch', 'source_too_large',
    'stable_identity_required', 'stored_original_corrupt', 'tombstone_content_mismatch',
    'unexpected_page_token', 'unknown_cycle', 'unknown_partition', 'unknown_source',
    'unsupported_source_filter', 'cursor_expired', 'transport_unavailable',
    'source_unavailable', 'selection_incomplete', 'selection_interrupted',
})
# The bridge crosses HTTP as 'bridge_<code>'; both forms are admitted so a
# prefixed failure name is never mistaken for foreign text.
SUMMARY_ERRORS = (BRIDGE_ERRORS
                  | {'bridge_' + code for code in BRIDGE_ERRORS
                     if not code.startswith('bridge_')}
                  | SYNC_ERRORS)


def _is_http_status_code(code):
    """Bounded HTTP status pattern from a status int, never free text."""
    return (isinstance(code, str) and code.startswith('http_')
            and code[5:].isdigit() and 1 <= len(code[5:]) <= 4)


def is_closed_code(code):
    """Closed membership incl. bounded http_<status> from status ints."""
    return (isinstance(code, str)
            and (code in SUMMARY_ERRORS or _is_http_status_code(code)))


def sanitize_adapter_error(code):
    """Adapter frontier filter: closed code or fixed generic, never raw text."""
    return code if is_closed_code(code) else 'source_unavailable'


def summary_error(info):
    """Map adapter state to the durable summary error: whitelist or generic."""
    code = (info.get('adapter') or {}).get('error') if isinstance(info, dict) else None
    return code if is_closed_code(code) else 'selection_incomplete'
