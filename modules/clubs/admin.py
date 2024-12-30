from django.contrib import admin

from .models import (
    Club,
)


class ClubAdmin(admin.ModelAdmin):
    """
    club dependency admin
    """

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'created_by', 'modified_by')


admin.site.register(Club, ClubAdmin)
