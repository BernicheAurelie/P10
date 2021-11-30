from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from registration.serializers import RegisterSerializer, UserSerializer, ProjectSerializer
from registration.models import Projects


class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

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

