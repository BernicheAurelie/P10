"""projet_10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens')
]

# projects_router = routers.SimpleRouter(trailing_slash=False)
# projects_router.register(r"projects/?", views.ProjectViewSet)

# users_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
# users_router.register(r"users/?", views.ContributorViewSet, basename="users")

# issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
# issues_router.register(r"issues/?", views.IssueViewSet, basename="issues")

# comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
# comments_router.register(r"comments/?", views.CommentViewSet, basename="comments")

# urlpatterns = [
#     path("", include(projects_router.urls)),
#     path("", include(users_router.urls)),
#     path("", include(issues_router.urls)),
#     path("", include(comments_router.urls)),
#     path("signup", views.RegisterApi.as_view()),
#     path("login", obtain_jwt_token),
# ]