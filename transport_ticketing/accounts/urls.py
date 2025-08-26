from django.urls import path
from .views import (
    UserRegistrationView,
    UserListView,
    LoginView,
    UserPromotionView
    )

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='list_view'),
    path("login/", LoginView.as_view(), name="login"),
    path('promote-user/', UserPromotionView.as_view(), name='promote-user'),


]
