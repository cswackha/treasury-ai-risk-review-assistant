"""Simple deterministic risk scoring logic."""

def calculate_risk_score(data_sensitivity: str, deployment_environment: str) -> int:
    score = 1

    if data_sensitivity.lower() in ["confidential", "financial", "pii", "taxpayer-related"]:
        score += 2

    if deployment_environment.lower() == "production":
        score += 2
    elif deployment_environment.lower() == "test":
        score += 1

    return min(score, 5)
