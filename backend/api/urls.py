from django.urls import path

from .views import (
    UserListView,
    RegisterView,
    LoginView,
    ActivityListCreateView,
)


urlpatterns = [

    # Users
    path(
        "users/",
        UserListView.as_view(),
        name="user-list"
    ),

    # Authentication
    path(
        "auth/register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "auth/login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
    "activities/",
    ActivityListCreateView.as_view(),
    name="activity-list-create"
),

]