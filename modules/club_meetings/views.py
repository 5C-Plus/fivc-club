from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    MeetingVenueFilterSet,
    MeetingFilterSet,
    MeetingRoleFilterSet,
    MeetingSessionFilterSet,
    MeetingSessionRoleBindingFilterSet,
)
from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
    MeetingSessionRoleBinding,
)
from .serializers import (
    MeetingVenueSerializer,
    MeetingSerializer,
    MeetingRoleSerializer,
    MeetingSessionSerializer,
    MeetingSessionRoleBindingSerializer,
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
    ).order_by('-time')
    serializer_class = MeetingSerializer


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
        'participant',
    ).prefetch_related(
        'participant__participant_titles',
        'participant__participant_titles__program',
        'participant__members',
        'participant__members__club',
    )
    serializer_class = MeetingRoleSerializer


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
    ).prefetch_related(
        'meeting_session_role_bindings',
        'meeting_session_role_bindings__meeting_role__participant',
    ).order_by('order')
    serializer_class = MeetingSessionSerializer


class MeetingSessionRoleBindingViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    filterset_class = MeetingSessionRoleBindingFilterSet
    lookup_field = 'uuid'
    queryset = MeetingSessionRoleBinding.objects.select_related(
        'created_by',
        'meeting_session',
        'meeting_role',
        'meeting_role__participant',
    ).all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = MeetingSessionRoleBindingSerializer
