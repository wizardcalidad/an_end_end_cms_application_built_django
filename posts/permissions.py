from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are allowed to the author of a post
        return obj.author == request.user

# class BasePermission(object):
#     """
#     A base class form which all permission classes should inherit.
#     """
#
#     def has_permission(self, request, view):
#         """
#         Return `True` if the permission is granted, `False` otherwise.
#         """
#         return True
#
#     def has_object_permission(self, request, view, obj):
#         """
#         Return `True` if the permission is granted, `False` otherwise.
#         """
#         return True
