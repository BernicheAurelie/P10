from rest_framework import serializers

from registration.models import Projects, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")
        

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        models = Projects
        fields = ['title', 'description', 'type', 'author_user_id']


# class ProjectDetailSerializer(serializers.ModelSerializer):
#     projects = serializers.SerializerMethodField()
#     class Meta:
#         model = Projects
#         fields = ['title', 'description', 'type', 'author_user_id']

#     def get_projects_user(self, instance, request):
#         # instance = instance de la catégorie consultée
#         # appelée autant de fois qu'il y a d'entité dans le cas d'une liste
#         queryset = instance.projects.filter(author_user_id=request.user)
#         serializer = ProjectSerializer(queryset, many=True)
#         return serializer.data
