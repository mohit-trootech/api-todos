from rest_framework.permissions import SAFE_METHODS
from accounts.models import User
from django.http import JsonResponse
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from utils.constants import JsonResponses
from django.core.exceptions import ValidationError


class ApiMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method not in SAFE_METHODS:
            try:
                api_key = request.GET.get("api_key", None)
                if api_key:
                    if not User.objects.filter(api_key=api_key).exists():
                        return JsonResponse(
                            {"details": JsonResponses.API_KEY_UNAUTHORIZED.value},
                            status=HTTP_401_UNAUTHORIZED,
                        )
            except ValidationError as err:
                return JsonResponse(
                    {"details": JsonResponses.INVALID_API.value},
                    status=HTTP_403_FORBIDDEN,
                )
        response = self.get_response(request)

        return response
