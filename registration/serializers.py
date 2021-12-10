from rest_framework import serializers

from registration.models import Comments, Contributors, Issues, Projects, User


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
        model = Projects
        fields = ['id', 'title', 'description', 'type', 'author_user_id']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = ['id', 'user_id', 'project_id', 'role']


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = [
            'id', 'title', 'desc', 'tag', 'priority', 'project_issue_id', 
            'status', 'author_id', 'assignee_user_id', 'created_time'
            ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'author_project_user_id', 'issue_id', 'description', 'created_time']

