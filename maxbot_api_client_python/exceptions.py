import httpx

class MaxBotException(Exception):
    default_message = "unexpected API error"
    
    def __init__(self, message: str | None = None, status_code: int | None = None, response: str | None = None):
        msg = message or self.default_message
        full_message = f"{msg}: status code {status_code}, response: {response}"
        super().__init__(full_message)
        self.status_code = status_code
        self.response = response

class ErrBadRequest(MaxBotException): default_message = "bad request"                  # 400
class ErrUnauthorized(MaxBotException): default_message = "unauthorized"               # 401
class ErrNotFound(MaxBotException): default_message = "not found"                      # 404
class ErrMethodNotAllowed(MaxBotException): default_message = "method not allowed"     # 405
class ErrTooManyRequests(MaxBotException): default_message = "too many requests"       # 429
class ErrServiceUnavailable(MaxBotException): default_message = "service unavailable"  # 503

def get_exception_for_status(status_code: int) -> type[MaxBotException]:
    error_map = {
        400: ErrBadRequest,
        401: ErrUnauthorized,
        404: ErrNotFound,
        405: ErrMethodNotAllowed,
        429: ErrTooManyRequests,
        503: ErrServiceUnavailable,
    }
    return error_map.get(status_code, MaxBotException)

def HandleErrorResponse(response: httpx.Response, body: bytes) -> Exception:
    status_code = response.status_code
    
    try:
        body_str = body.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"Failed to decode error response body as UTF-8 (status {status_code}): {e}")
        body_str = body.decode('utf-8', errors='replace')

    ExceptionClass = get_exception_for_status(status_code)
    
    return ExceptionClass(status_code=status_code, response=body_str)