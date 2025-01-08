from django.contrib import admin

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
)

admin.site.register(MeetingVenue)
admin.site.register(Meeting)
admin.site.register(MeetingSession)
admin.site.register(MeetingRole)
