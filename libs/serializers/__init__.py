from rest_framework import serializers


class SimpleSerializer(serializers.Serializer):

    def create(self, validated_data):
        raise AssertionError('not allowed')

    def update(self, instance, validated_data):
        raise AssertionError('not allowed')


class DictSerializer(serializers.Serializer):

    def create(self, validated_data):
        return {**validated_data}

    def update(self, instance, validated_data):
        instance.update(validated_data)
        return instance


class TrackableCreateModelSerializer(
    serializers.ModelSerializer
):
    created_by = serializers.ReadOnlyField(
        source='created_by.username',
        default='',
    )

    def create(self, validated_data):
        req = self.context.get('request')
        req_user = req and req.user
        req_user = req_user and req_user.is_authenticated or None
        validated_data['created_by'] = req_user
        return super().create(validated_data)


class TrackableModelSerializer(
    TrackableCreateModelSerializer
):
    modified_by = serializers.ReadOnlyField(
        source='modified_by.username',
        default='',
    )

    def create(self, validated_data):
        req = self.context.get('request')
        req_user = req and req.user
        req_user = req_user and req_user.is_authenticated or None
        validated_data['modified_by'] = req_user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        req = self.context.get('request')
        req_user = req and req.user
        req_user = req_user and req_user.is_authenticated or None
        validated_data['modified_by'] = req_user
        return super().update(instance, validated_data)

# class UserLoginSerializer(DictSerializer):
#     username = serializers.CharField(
#         required=True,
#         write_only=True,
#     )
#     password = serializers.CharField(
#         required=True,
#         write_only=True,
#     )
#     access_token = serializers.CharField(
#         read_only=True,
#     )
#
#
# class UserSelfSerializer(DictSerializer):
#     username = serializers.CharField(
#         read_only=True,
#     )
#     email = serializers.CharField(
#         read_only=True,
#     )
#     first_name = serializers.CharField(
#         read_only=True,
#     )
#     last_name = serializers.CharField(
#         read_only=True,
#     )
#     is_staff = serializers.BooleanField(
#         read_only=True,
#     )
#     is_active = serializers.BooleanField(
#         read_only=True,
#     )
#     date_joined = serializers.DateTimeField(
#         read_only=True,
#     )
