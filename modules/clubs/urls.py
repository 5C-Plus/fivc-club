from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    ClubViewSet,
)

app_name = 'clubs'

router = DefaultRouter()
router.register(
    'clubs',
    ClubViewSet,
    basename='clubs',
)

urlpatterns = [
    path('', include(router.urls))
]
