from django.urls import path
from registration.views import RegisterApi

app_name = "registration"

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register')
]
