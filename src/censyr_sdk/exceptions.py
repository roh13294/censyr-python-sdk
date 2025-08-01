class CensyrSDKError(Exception):
    """Base exception for all Censyr SDK errors."""
    pass

class AuthenticationError(CensyrSDKError):
    pass

class RateLimitError(CensyrSDKError):
    pass

class APIError(CensyrSDKError):
    pass

class ValidationError(CensyrSDKError):
    pass

class NotFoundError(CensyrSDKError):
    pass

class ForbiddenError(CensyrSDKError):
    pass
