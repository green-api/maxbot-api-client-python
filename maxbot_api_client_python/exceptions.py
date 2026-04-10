import httpx

class MaxBotError(Exception):
    default_message = "unexpected API error"
    
    def __init__(self, message: str | None = None, status_code: int | None = None, response: str | None = None):
        msg = message or self.default_message
        full_message = f"{msg}: status code {status_code}, response: {response}"
        super().__init__(full_message)
        self.status_code = status_code
        self.response = response

class BadRequestError(MaxBotError): default_message = "bad request"
class UnauthorizedError(MaxBotError): default_message = "unauthorized"
class NotFoundError(MaxBotError): default_message = "not found"
class MethodNotAllowedError(MaxBotError): default_message = "method not allowed"
class TooManyRequestsError(MaxBotError): default_message = "too many requests"
class ServiceUnavailableError(MaxBotError): default_message = "service unavailable"

_ERROR_MAP = {
    400: BadRequestError,
    401: UnauthorizedError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    429: TooManyRequestsError,
    503: ServiceUnavailableError,
}

def get_exception_for_status(status_code: int) -> type[MaxBotError]:
    return _ERROR_MAP.get(status_code, MaxBotError)

def build_api_error(response: httpx.Response) -> MaxBotError:
    body_str = response.content[:1000].decode('utf-8', errors='replace') 
    ExceptionClass = get_exception_for_status(response.status_code)
    
    return ExceptionClass(status_code=response.status_code, response=body_str)