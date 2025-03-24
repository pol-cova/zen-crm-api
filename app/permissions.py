from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only business owners to modify their own data.
    """

    def has_permission(self, request, view):
        # For list views, we'll rely on filtering in get_queryset
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user