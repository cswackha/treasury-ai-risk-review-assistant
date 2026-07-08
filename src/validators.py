"""Input validation helpers."""

def is_valid_use_case(text: str) -> bool:
    return bool(text and text.strip())
