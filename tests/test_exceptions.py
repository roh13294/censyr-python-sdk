import pytest
import censyr_sdk

class DummyError(Exception):
    pass

def test_exceptions_exist():
    expected_exceptions = [
        "CensyrSDKError",
        "AuthenticationError",
        "RateLimitError",
        "APIError",
        "ValidationError",
        "NotFoundError",
        "ForbiddenError",
    ]
    for exc in expected_exceptions:
        assert hasattr(censyr_sdk, exc), f"Missing exception class: {exc}"
