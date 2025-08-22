from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    message = "Only admin users can modify data."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access for all users
        return request.user.is_authenticated and request.user.role == 'admin'