"""xxx URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import authentication, permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Fivc Club API',
        default_version='V1',
        description='Fivc Club',
    ),
    public=True,
    authentication_classes=[authentication.SessionAuthentication],
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/documents/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/admin/', admin.site.urls),
    path('api/drf/', include('rest_framework.urls')),
    path('api/', include('modules.club_accounts.urls')),
    path('api/', include('modules.club_participants.urls')),
    path('api/', include('modules.club_meetings.urls')),
    path('api/', include('modules.clubs.urls')),
    path('api/', include('modules.user_socials.urls')),
    path('api/', include('modules.users.urls')),
]
