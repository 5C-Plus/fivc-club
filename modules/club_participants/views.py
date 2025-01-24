from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    ParticipantFilterSet,
    ParticipantTitleFilterSet,
    MemberFilterSet,
)
from .models import (
    Participant,
    ParticipantTitle,
    Member,
)
from .serializers import (
    ParticipantSerializer,
    ParticipantTitleSerializer,
    MemberSerializer,
)


class ParticipantViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    participants view set
    """
    filterset_class = ParticipantFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Participant.objects.select_related(
        'created_by',
        'modified_by',
    ).prefetch_related(
        'members',
        'members__club',
    ).all()
    serializer_class = ParticipantSerializer


class ParticipantTitleViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    participant title view set
    """
    filterset_class = ParticipantTitleFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = ParticipantTitle.objects.select_related(
        'program',
        'participant',
        'created_by',
        'modified_by',
    ).all()
    serializer_class = ParticipantTitleSerializer


class MemberViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    participants view set
    """
    filterset_class = MemberFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Member.objects.select_related(
        'club',
        'participant',
        'created_by',
        'modified_by',
    ).all()
    serializer_class = MemberSerializer
