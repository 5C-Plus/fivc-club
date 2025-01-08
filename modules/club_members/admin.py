from django.contrib import admin

from .models import (
    Attendee,
    Membership,
)


admin.site.register(Attendee)
admin.site.register(Membership)
