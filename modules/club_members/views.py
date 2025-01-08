from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    AttendeeFilterSet,
    MembershipFilterSet,
)
from .models import (
    Attendee,
    Membership,
)
from .serializers import (
    AttendeeSerializer,
    MembershipSerializer,
)


class AttendeeViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    attendee view set
    """
    filterset_class = AttendeeFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Attendee.objects.select_related(
        'created_by',
        'modified_by',
    ).all()
    serializer_class = AttendeeSerializer


class MembershipViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    attendee view set
    """
    filterset_class = MembershipFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Membership.objects.select_related(
        'club',
        'attendee',
        'created_by',
        'modified_by',
    ).all()
    serializer_class = MembershipSerializer
