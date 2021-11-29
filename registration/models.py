from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=88)

    
    # user_id = models.IntegerField(auto_created=True)
        # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=88)
    # password = models.CharField(max_length=12)
    # password2 = models.CharField(max_length=12)

