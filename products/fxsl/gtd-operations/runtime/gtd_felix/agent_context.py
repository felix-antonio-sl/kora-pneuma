"""Agent presentation only: authoritative records and validity bases stay intact."""


ASSESSMENT_BASES = frozenset({'resolution_basis', 'material_basis'})


def agent_item(item):
    """Keep all meaning/evidence, omitting only nested validation snapshots."""
    if not isinstance(item, dict):
        return item
    result = dict(item)
    assessments = item.get('assessments')
    if isinstance(assessments, list):
        omitted = sorted({key for assessment in assessments if isinstance(assessment, dict)
                          for key in ASSESSMENT_BASES if key in assessment})
        result['assessments'] = [
            {key: value for key, value in assessment.items() if key not in ASSESSMENT_BASES}
            if isinstance(assessment, dict) else assessment for assessment in assessments]
        if omitted:
            result['_presentation'] = {'omitted_assessment_fields': omitted,
                'full_record': {'view': 'item', 'item_id': item.get('id'), 'detail': 'full'}}
    return result
