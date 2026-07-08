from src.validators import is_valid_use_case

def test_valid_use_case():
    assert is_valid_use_case("Classify policy documents") is True

def test_empty_use_case():
    assert is_valid_use_case("   ") is False
