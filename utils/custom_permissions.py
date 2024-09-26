from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


class ApiPermissionOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    api_key = None

    def has_api(self, request):
        """
        checks if Request Has Api Key
        """
        self.api_key = request.GET.get("api_key", None)
        if self.api_key:
            return True
        return False

    def has_permission(self, request, view):
        """checks for permissions"""
        return bool(request.method in SAFE_METHODS or self.has_api(request))
