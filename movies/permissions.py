from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser and request.user.is_staff:
            return True

        if request.method == "GET":
            return True

        return False


class CriticPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser and request.user.is_staff:
            return True

        return False


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser and not request.user.is_staff:
            return True

        return False
