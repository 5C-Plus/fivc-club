from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    UserSelfView,
    UserPreferenceView,
)

app_name = 'users'

urlpatterns = [
    path(
        'users/login/',
        UserLoginView.as_view(),
        name='login'
    ),
    path(
        'users/logout/',
        UserLogoutView.as_view(),
        name='logout'
    ),
    path(
        'users/self/',
        UserSelfView.as_view(),
        name='self'
    ),
    path(
        'users/preference/',
        UserPreferenceView.as_view(),
        name='preference'
    ),
]
