

import json
from typing import Any, Dict, Optional, Union


def _extract_usage(obj: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Extract usage stats when the event carries an empty choices list."""
    if obj.get("choices") == [] and obj.get("usage"):
        return {"usage": obj["usage"]}
    return None


def _extract_patch_value(patch: Dict[str, Any]) -> Optional[str]:
    """Extract a text value from a single markdown_block patch."""
    value = patch.get("value")
    if isinstance(value, dict):
        value = value.get("answer") or ""
    if isinstance(value, str) and value:
        return value
    return None


def _extract_blocks_markdown(obj: Dict[str, Any]) -> Optional[str]:
    """Extract markdown text delta from the "blocks" diff structure."""
    if "blocks" not in obj:
        return None

    for block in obj.get("blocks", []):
        diff = block.get("diff_block") or {}
        if diff.get("field") != "markdown_block":
            continue
        for patch in diff.get("patches", []):
            value = _extract_patch_value(patch)
            if value:
                return value

    return None


def _extract_choices_content(obj: Dict[str, Any]) -> Optional[str]:
    """Extract text delta from the standard "choices[0].delta.content" path."""
    choices = obj.get("choices") or []
    if not choices:
        return None

    delta = choices[0].get("delta") or {}
    content = delta.get("content")
    if content:
        return content

    return None


def parse_sse_line(data_str: str) -> Optional[Union[str, Dict[str, Any]]]:
    """Parse a single SSE data line from Perplexity's streaming response.

    Extracts text content, thinking summaries, or usage statistics from
    the JSON-encoded SSE event data.

    Args:
        data_str: The raw data string (after "data: " prefix stripped).

    Returns:
        A string (text delta), a dict (usage info), or None if unparseable.
    """
    try:
        obj = json.loads(data_str)
    except json.JSONDecodeError:
        return None

    usage = _extract_usage(obj)
    if usage is not None:
        return usage

    markdown = _extract_blocks_markdown(obj)
    if markdown is not None:
        return markdown

    content = _extract_choices_content(obj)
    if content is not None:
        return content

    return None
