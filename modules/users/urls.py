from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    UserSelfView,
)

app_name = 'users'

urlpatterns = [
    path('users/login/', UserLoginView.as_view()),
    path('users/logout/', UserLogoutView.as_view()),
    path('users/self/', UserSelfView.as_view()),
]
