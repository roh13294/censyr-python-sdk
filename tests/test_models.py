import pytest
import censyr_sdk

def test_models_exist():
    expected_models = [
        "Model",
        "Inference",
        "Violation",
        "AuditLog",
        "CustomRule",
    ]
    for model in expected_models:
        assert hasattr(censyr_sdk, model), f"Missing model class: {model}"
