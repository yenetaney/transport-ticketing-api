from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and 
            request.user.role in ['super_admin', 'company_admin']
        )
    
class CanManageOwnCompanyObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'company'):
            return request.user.role == 'company_admin' and obj.company == request.user.company
        if hasattr(obj, 'trip') and hasattr(obj.trip, 'company'):
            return request.user.role == 'company_admin' and obj.trip.company == request.user.company
        return False
    
class IsSuperAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'super_admin'
