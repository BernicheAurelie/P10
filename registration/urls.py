from django.urls import path, include
from registration.views import RegisterApi, ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

app_name = "registration"


projects_router = SimpleRouter(trailing_slash=False)
projects_router.register(r"projects/?", ProjectViewSet, basename='projects')

users_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorViewSet, basename="users")

issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
issues_router.register(r"issues/?", IssueViewSet, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
comments_router.register(r"comments/?", CommentViewSet, basename="comments")

urlpatterns = [
    path('signup/', RegisterApi.as_view(), name='register'),
    path('', include(projects_router.urls)),
    path('', include(users_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls))
]
