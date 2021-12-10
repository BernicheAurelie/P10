from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAuhtorFromTheProject(BasePermission):
 
    def has_object_permission(self, request, view, project):
        return project.author_user_id == request.user
        #  return bool(request.user==request.data["author_user_id"])


class IsContributorFromTheProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        pass