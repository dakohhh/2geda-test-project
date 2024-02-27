from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed
import rest_framework.status as status
from client import CustomResponse

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        detail_message = str(exc.detail) if exc.detail else "Authentication failed"

        response = CustomResponse(message=detail_message, status=status.HTTP_401_UNAUTHORIZED)

    return response
