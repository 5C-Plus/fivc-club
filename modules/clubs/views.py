from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    ClubFilterSet,
    ProgramFilterSet
)
from .models import (
    Club,
    Program
)
from .serializers import (
    ClubSerializer,
    ProgramSerializer
)


class ClubViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    club view set
    """
    filterset_class = ClubFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Club.objects.select_related(
        'created_by',
        'modified_by',
    ).all()
    serializer_class = ClubSerializer


class ProgramViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    """
    program view set
    """
    filterset_class = ProgramFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Program.objects.select_related(
        'created_by',
        'modified_by',
    ).all()
    serializer_class = ProgramSerializer
