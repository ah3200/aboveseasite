from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners (author) of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
        
