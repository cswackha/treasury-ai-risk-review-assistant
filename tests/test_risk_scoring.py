from src.risk_scoring import calculate_risk_score

def test_low_risk_score():
    assert calculate_risk_score("public", "prototype") == 1

def test_high_risk_score_capped_at_five():
    assert calculate_risk_score("pii", "production") == 5
