from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    ClubViewSet,
    ProgramViewSet,
)

app_name = 'clubs'

router = DefaultRouter()
router.register(
    'clubs/programs',
    ProgramViewSet,
    basename='club_programs',
)
router.register(
    'clubs',
    ClubViewSet,
    basename='clubs',
)

urlpatterns = [
    path('', include(router.urls))
]
