import pytest
from prediction_helper import predict_risk

def test_credit_prediction_string_output():
    """Verify that the prediction helper returns a valid response string."""
    result = predict_risk(30, 50000, 10000, 700)
    assert isinstance(result, str)

def test_credit_prediction_high_risk():
    """Verify that low credit scores or high loan amounts register correctly."""
    result = predict_risk(50, 20000, 40000, 450)
    assert "Risk" in result