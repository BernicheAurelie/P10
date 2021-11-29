from rest_framework import serializers

from registration.models import User


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

# class RegistrationSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']

#     def save(self):
#         user = User(
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name'],
#             email=self.validated_data['email']
#         )
#         password = self.validated_data['password']

#         user.set_password(password)
#         user.save()
#         return user
