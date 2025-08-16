from django.urls import path
from .views import (
    UserRegistrationView,
    UserListView,
    LoginView,
    )

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='list_view'),
    path("login/", LoginView.as_view(), name="login"),

]
