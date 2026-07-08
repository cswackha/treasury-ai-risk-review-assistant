"""AI response handling for the Treasury AI Risk Review Assistant."""

def generate_mock_assessment(use_case: str) -> str:
    """Return a deterministic mock assessment when no live AI key is configured."""
    return f"""
Mock AI Assessment for: {use_case}

Risk Level: Medium

Recommended Controls:
- Require human review before action
- Validate input data quality
- Apply access control
- Log review activity
- Conduct cybersecurity and privacy review before production deployment
"""
