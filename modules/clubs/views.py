from rest_framework import viewsets

from libs.permissions import IsAdminOrReadOnly
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import ClubFilterSet
from .models import Club
from .serializers import ClubSerializer


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
