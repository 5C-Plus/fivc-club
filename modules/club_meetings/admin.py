from django.contrib import admin

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
    MeetingSessionRoleBinding,
)

admin.site.register(MeetingVenue)
admin.site.register(Meeting)
admin.site.register(MeetingRole)
admin.site.register(MeetingSession)
admin.site.register(MeetingSessionRoleBinding)
