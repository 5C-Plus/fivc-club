from rest_framework import serializers


def trackable_create(modify=True):
    def _decorator(create_func):
        def _create(self, validated_data):
            request = self.context.get('request')
            user = request and request.user or None
            validated_data['created_by'] = user
            if modify:
                validated_data['modified_by'] = user
            return create_func(self, validated_data)

        return _create

    return _decorator


def trackable_update(modify=True):
    def _decorator(update_func):
        if not modify:
            return update_func

        def _update(self, instance, validated_data):
            request = self.context.get('request')
            user = request and request.user or None
            validated_data['modified_by'] = user
            return update_func(
                self, instance, validated_data)

        return _update

    return _decorator


def trackable_serializer(modify=True):
    def _decorator(serializer_cls):
        assert issubclass(
            serializer_cls, serializers.Serializer)
        serializer_cls.create = trackable_create(
            modify=modify
        )(serializer_cls.create)
        serializer_cls.update = trackable_update(
            modify=modify
        )(serializer_cls.update)
        return serializer_cls

    return _decorator
