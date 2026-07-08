"""AI response handling for the Treasury AI Risk Review Assistant."""

import os

import streamlit as st
from openai import OpenAI

from src.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


def get_secret_value(name: str, default: str | None = None) -> str | None:
    """Read a value from Streamlit secrets or environment variables."""
    try:
        if name in st.secrets:
            return st.secrets[name]
    except Exception:
        pass

    return os.getenv(name, default)


def generate_mock_assessment(use_case_name: str) -> str:
    """Return a deterministic mock assessment when no live AI key is configured."""
    return f"""
### 1. Use Case Summary
The proposed use case, **{use_case_name}**, would use AI to support review, analysis, or prioritization activities.

### 2. Potential Benefits
- Reduces manual review time
- Improves consistency
- Supports faster decision-making
- Helps identify risks earlier in the process

### 3. Data Sensitivity Concerns
The use case should be reviewed for personally identifiable information, financial data, taxpayer-related data, internal-only data, or other sensitive information before production deployment.

### 4. Cybersecurity Risks
Potential risks include unauthorized access, prompt injection, data leakage, model misuse, weak logging, and lack of auditability.

### 5. Operational Risks
The system should not be used as the sole decision-maker. Human review is required before action is taken.

### 6. Human-in-the-Loop Recommendations
- Require analyst review before final decisions
- Log review activity
- Clearly label AI-generated recommendations
- Escalate high-risk results to appropriate leadership or security review

### 7. Deployment Readiness
**Readiness: Prototype / Test Environment**

The solution is suitable for demonstration and controlled testing, but not production use without additional controls.

### 8. Recommended Controls Before Production
- Access control
- Audit logging
- Cybersecurity review
- Privacy review
- Model monitoring
- Human approval workflow
- Prompt injection testing
- Data retention review

### 9. Assumptions
This mock assessment assumes no sensitive Treasury data is used and that the system is advisory only.
"""


def generate_ai_assessment(
    use_case_name: str,
    business_objective: str,
    data_sensitivity: str,
    deployment_environment: str,
    planned_controls: str,
) -> tuple[str, str]:
    """
    Generate an AI assessment using OpenAI when configured.
    Falls back to mock mode when no API key is available.
    Returns: assessment text, mode used.
    """

    api_key = get_secret_value("OPENAI_API_KEY")
    model = get_secret_value("AI_MODEL", "gpt-4o-mini")

    if not api_key:
        return generate_mock_assessment(use_case_name), "Mock mode - no API key configured"

    try:
        client = OpenAI(api_key=api_key)

        user_prompt = USER_PROMPT_TEMPLATE.format(
            use_case_name=use_case_name,
            business_objective=business_objective,
            data_sensitivity=data_sensitivity,
            deployment_environment=deployment_environment,
            planned_controls=planned_controls,
        )

        response = client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=user_prompt,
        )

        return response.output_text, f"Live AI mode - model: {model}"

    except Exception as exc:
        fallback = generate_mock_assessment(use_case_name)
        return (
            f"""
### Live AI Call Failed

The application fell back to deterministic mock mode so the workflow remains testable.

**Error summary:** {exc}

---

{fallback}
""",
            "Fallback mock mode - AI call failed",
        )