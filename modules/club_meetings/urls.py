from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    MeetingVenueViewSet,
    MeetingViewSet,
    MeetingRoleViewSet,
    MeetingSessionViewSet,
    MeetingSessionRoleBindingViewSet,
)

app_name = 'club_meetings'

router = DefaultRouter()
router.register(
    'meetings/venues',
    MeetingVenueViewSet,
    basename='meeting_venues',
)
router.register(
    'meetings/roles',
    MeetingRoleViewSet,
    basename='meeting_roles',
)
router.register(
    'meetings/sessions',
    MeetingSessionViewSet,
    basename='meeting_sessions',
)
router.register(
    'meetings/session-role-bindings',
    MeetingSessionRoleBindingViewSet,
    basename='meeting_session_role_bindings',
)
router.register(
    'meetings',
    MeetingViewSet,
    basename='meetings',
)

urlpatterns = [
    path('', include(router.urls))
]
