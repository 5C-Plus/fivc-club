import random
import time

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
from django.db import (
    transaction,
    IntegrityError,
    OperationalError,
)
from rest_framework import (
    exceptions,
    response,
    views,
    viewsets,
)

from .serializers import (
    UserLoginSerializer,
    UserSelfSerializer,
    UserSelfUpdateSerializer,
    UserPreferenceSerializer,
    UserChangePasswordSerializer,
    UserSetPasswordSerializer,
)
from .models import (
    UserPreference,
)


def retry_db_operation(func, max_retries=3, base_delay=0.1):
    """
    Retry database operations that might fail due to locking
    """
    for attempt in range(max_retries):
        try:
            return func()
        except (OperationalError, IntegrityError) as e:
            if 'database is locked' in str(
                    e).lower() and attempt < max_retries - 1:
                # Exponential backoff with jitter
                delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
                time.sleep(delay)
                continue
            raise e


class UserLoginView(views.APIView):
    """
    user login api
    """

    permission_classes = ()

    # @csrf.csrf_exempt
    def post(self, request, *args, **kwargs):
        ser = UserLoginSerializer(
            data=request.data,
            context=self.get_renderer_context())
        ser.is_valid(raise_exception=True)
        ser_data = ser.save()

        # authenticate user
        user = authenticate(
            request,
            username=ser_data['username'],
            password=ser_data['password'],
        )
        if not user or not user.is_active:
            raise exceptions.AuthenticationFailed('fail to login')

        # login user
        login(request, user)

        if not request.session.session_key:
            request.session.create()

        ser_data.update(
            access_token=request.session.session_key)

        ser = UserLoginSerializer(
            instance=ser_data,
            context=self.get_renderer_context(),
        )
        return response.Response(ser.data)


class UserLogoutView(views.APIView):
    """
    user logout api
    """

    def post(self, request, *args, **kwargs):
        logout(request)
        return response.Response()


class UserSelfView(views.APIView):
    """
    user self api
    """
    permission_classes = ()  # 在视图内部进行认证检查

    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        ser = UserSelfSerializer(
            instance={
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined,
            },
            context=self.get_renderer_context()
        )
        return response.Response(ser.data)

    def patch(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        ser = UserSelfUpdateSerializer(
            instance=user,
            data=request.data,
            context=self.get_renderer_context(),
            partial=True
        )
        ser.is_valid(raise_exception=True)
        updated_user = ser.save()

        # 返回更新后的用户信息
        response_ser = UserSelfSerializer(
            instance={
                'username': updated_user.username,
                'email': updated_user.email,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'is_staff': updated_user.is_staff,
                'is_active': updated_user.is_active,
                'date_joined': updated_user.date_joined,
            },
            context=self.get_renderer_context()
        )
        return response.Response(response_ser.data)


class UserPreferenceView(views.APIView):
    """
    user preference api
    """

    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        def _get_preference():
            with transaction.atomic():
                instance, _ = UserPreference.objects.get_or_create(
                    user=user,
                    defaults={},
                )
                ser = UserPreferenceSerializer(
                    instance=instance,
                    context=self.get_renderer_context()
                )
                return ser.data

        # Retry the operation if database is locked
        data = retry_db_operation(_get_preference)
        return response.Response(data)

    def patch(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        def _update_preference():
            with transaction.atomic():
                # Use get_or_create with proper error handling
                instance, created = UserPreference.objects.get_or_create(
                    user=user,
                    defaults={}
                )

                ser = UserPreferenceSerializer(
                    instance=instance,
                    data=request.data,
                    context=self.get_renderer_context(),
                    partial=True,
                )
                ser.is_valid(raise_exception=True)
                ser.save()
                return ser.data

        # Retry the operation if database is locked
        data = retry_db_operation(_update_preference)
        return response.Response(data)


class UserChangePasswordView(views.APIView):
    """
    用户修改密码API
    """
    permission_classes = ()  # 在视图内部进行认证检查

    def post(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        ser = UserChangePasswordSerializer(
            data=request.data,
            context=self.get_renderer_context()
        )
        ser.is_valid(raise_exception=True)
        result = ser.save()

        return response.Response(result)


class UserPreferenceViewSet(viewsets.ModelViewSet):

    lookup_field = 'uuid'
    queryset = UserPreference.objects.select_related(
        'user',
    ).all()
    serializer_class = UserPreferenceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__username=self.request.user.username)
        return qs


class UserSetPasswordView(views.APIView):
    """
    管理员设置用户密码API
    """
    permission_classes = ()  # 在视图内部进行认证检查

    def post(self, request, username, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated('anonymous user')

        if not user.is_staff:
            raise exceptions.PermissionDenied('只有管理员可以设置用户密码')

        # 获取目标用户
        User = get_user_model()
        try:
            target_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.NotFound(f'用户 {username} 不存在')

        ser = UserSetPasswordSerializer(
            data=request.data,
            context={
                **self.get_renderer_context(),
                'target_user': target_user
            }
        )
        ser.is_valid(raise_exception=True)
        result = ser.save()

        return response.Response(result)
