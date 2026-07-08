"""Prompt templates for the Treasury AI Risk Review Assistant."""

SYSTEM_PROMPT = """
You are an AI risk review assistant supporting a secure government technology assessment workflow.
Your role is to provide structured, practical, and cautious analysis of proposed AI use cases.

You must:
- Identify cybersecurity, privacy, operational, and data sensitivity risks.
- Recommend human-in-the-loop controls.
- Avoid making final authorization decisions.
- Clearly state assumptions.
- Provide concise, professional recommendations suitable for executive and technical review.
"""

USER_PROMPT_TEMPLATE = """
Review the following proposed AI use case.

Use Case Name:
{use_case_name}

Business Objective:
{business_objective}

Data Sensitivity:
{data_sensitivity}

Deployment Environment:
{deployment_environment}

Controls Already Planned:
{planned_controls}

Provide a structured review with the following sections:

1. Use Case Summary
2. Potential Benefits
3. Data Sensitivity Concerns
4. Cybersecurity Risks
5. Operational Risks
6. Human-in-the-Loop Recommendations
7. Deployment Readiness
8. Recommended Controls Before Production
9. Assumptions
"""
