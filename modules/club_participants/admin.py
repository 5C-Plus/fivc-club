from django.contrib import admin

from .models import (
    Participant,
    ParticipantTitle,
    Member,
)


admin.site.register(Participant)
admin.site.register(ParticipantTitle)
admin.site.register(Member)
