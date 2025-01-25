from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):    # Permission for checking whether user is doctor or not
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated: # if the user does not exist or has not been authenticated
            return False
        if request.user.role != 'doctor': # checking the user role
            return False
        return True
