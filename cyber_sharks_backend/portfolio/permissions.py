# portfolio/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a portfolio to edit or delete it.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner or admins
        return obj.user == request.user or request.user.is_staff
