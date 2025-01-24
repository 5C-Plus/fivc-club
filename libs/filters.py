from django.forms import fields
from django_filters.rest_framework import (
    filters,
)


class DummyFilter(filters.CharFilter):

    def filter(self, qs, value):
        return qs  # do nothing


class NullUUIDField(fields.UUIDField):
    def to_python(self, value):
        return None if value == 'null' else super().to_python(value)


class NullUUIDFilter(filters.UUIDFilter):
    field_class = NullUUIDField


# class NullCharField(fields.CharField):
#     def to_python(self, value):
#         return None if value == 'null' else super().to_python(value)
#
#
# class NullCharFilter(filters.CharFilter):
#     field_class = NullCharField
