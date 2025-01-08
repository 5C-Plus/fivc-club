from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    MeetingVenueFilterSet,
    MeetingFilterSet,
    MeetingSessionFilterSet,
    MeetingRoleFilterSet,
)
from .models import (
    MeetingVenue,
    Meeting,
    MeetingSession,
    MeetingRole,
)
from .serializers import (
    MeetingVenueSerializer,
    MeetingSerializer,
    MeetingSessionSerializer,
    MeetingRoleSerializer,
)


class MeetingVenueViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    meeting venue
    """
    filterset_class = MeetingVenueFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = MeetingVenue.objects.select_related(
        'created_by',
        'modified_by',
        'club',
    )
    serializer_class = MeetingVenueSerializer


class MeetingViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = MeetingFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Meeting.objects.select_related(
        'created_by',
        'modified_by',
        'club',
        'venue',
        'meeting_manager',
    )
    serializer_class = MeetingSerializer


class MeetingSessionViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = MeetingSessionFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = MeetingSession.objects.select_related(
        'created_by',
        'modified_by',
        'meeting',
    )
    serializer_class = MeetingSessionSerializer


class MeetingRoleViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = MeetingRoleFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = MeetingRole.objects.select_related(
        'created_by',
        'modified_by',
        'meeting',
        'meeting_session',
        'attendee',
    )
    serializer_class = MeetingRoleSerializer
