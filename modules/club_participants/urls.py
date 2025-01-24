from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    ParticipantViewSet,
    ParticipantTitleViewSet,
    MemberViewSet,
)

app_name = 'club_participants'

router = DefaultRouter()
router.register(
    'participants/members',
    MemberViewSet,
    basename='participant_members',
)
router.register(
    'participants/titles',
    ParticipantTitleViewSet,
    basename='participant_titles',
)
router.register(
    'participants',
    ParticipantViewSet,
    basename='participants',
)


urlpatterns = [
    path('', include(router.urls))
]
