from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    AttendeeViewSet,
    MembershipViewSet,
)

app_name = 'club_members'

router = DefaultRouter()
router.register(
    'members/attendees',
    AttendeeViewSet,
    basename='member_attendees',
)
router.register(
    'members/membership',
    MembershipViewSet,
    basename='member_membership',
)

urlpatterns = [
    path('', include(router.urls))
]
