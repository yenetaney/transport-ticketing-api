from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
     message = "Only admin users can perform this action."
     def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'