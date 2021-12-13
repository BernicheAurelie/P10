from rest_framework.permissions import IsAuthenticated, BasePermission
from registration.models import Contributors


class IsAuhtorFromTheProject(BasePermission):
 
    def has_object_permission(self, request, view, project):
        print("you're the author")
        return project.author_user_id == request.user
        #  return bool(request.user==request.data["author_user_id"])


class IsContributorFromTheProject(BasePermission):

    def has_object_permission(self, request, view, project):
        contributor = Contributors.objects.get(project_id = project.id)
        print("permission?")
        if request.user == contributor.user_id:
            print("Allowed: You're contributor")
            return True
        else:
            print("Acces denied: You're not contributor for the project")
            return False