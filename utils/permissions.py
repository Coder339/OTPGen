from rest_framework import permissions


class AnonPermission(permissions.BasePermission):
    """
    Non Auth users only
    """
    message = 'you are already authenticated'

    def has_permission(self, request, view):
        # return not request.user.is_authenticated() -> this was for django 2.0  
        return request.user.is_authenticated




class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message  = 'may be you are not the owner of it'
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user




class IsSuper(permissions.BasePermission):
    """Grants admins full access"""
    message  = 'you are not the superuser'
    def has_permission(self, request, view):
        return request.user.is_staff