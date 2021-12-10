from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from registration.serializers import ContributorSerializer, IssueSerializer, RegisterSerializer, UserSerializer, ProjectSerializer, CommentSerializer
from registration.models import Comments, Contributors, Issues, Projects
from registration.permissions import IsAuhtorFromTheProject, IsContributorFromTheProject


class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, IsAuhtorFromTheProject | IsContributorFromTheProject)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        return Projects.objects.filter(author_user_id=self.request.user)

    # def get_queryset(self):
    #     queryset = Projects.objects.all()
    #     author_user_id = self.request.GET.get('author_user_id')
    #     author_user_id = self.request.query_params.get('author_user_id')
    #     if author_user_id == self.request.user:
    #         queryset = queryset.filter(author_user_id=author_user_id)
    #     return queryset

class ContributorViewSet(ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_id"] = kwargs['projects_pk']
        request.POST._mutable = False
        return super(ContributorViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_id"] = kwargs['projects_pk']
        request.POST._mutable = False
        return super(ContributorViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        return Contributors.objects.filter(project_id = self.kwargs['projects_pk'])


class IssueViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_issue_id"] = kwargs['projects_pk']
        project = Projects.objects.filter(id=kwargs['projects_pk'])
        project_author_id= project[0].author_user_id.id
        request.data["author_id"] = project_author_id
        # request.data["author_id"] = project.get('author_user_id')
        request.POST._mutable = False
        return super(IssueViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_issue_id"] = kwargs['projects_pk']
        project = Projects.objects.filter(id=kwargs['projects_pk'])
        project_author_id= project[0].author_user_id.id
        request.data["author_id"] = project_author_id
        request.POST._mutable = False
        return super(IssueViewSet, self).update(request, *args, **kwargs)
    
    def get_queryset(self):
        return Issues.objects.filter(project_issue_id = self.kwargs['projects_pk'])


class CommentViewSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = kwargs['issues_pk']
        issue = Issues.objects.filter(id=kwargs['issues_pk'])
        issue_author_id= issue[0].author_id.id
        request.data["author_project_user_id"] = issue_author_id
        request.POST._mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = kwargs['issues_pk']
        issue = Issues.objects.filter(id=kwargs['issues_pk'])
        issue_author_id= issue[0].author_id.id
        request.data["author_project_user_id"] = issue_author_id
        request.POST._mutable = False
        return super(CommentViewSet, self).update(request, *args, **kwargs)


@permission_classes([])
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )

