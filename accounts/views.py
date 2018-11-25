from django.db import transaction
from django.http import Http404

from .serializer import AccountSerializer
from .models import Account #,  SpaUser

from rest_framework import status
from rest_framework import permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
import uuid

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ユーザ情報取得のView(GET)
class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(data={
            'user_id': request.user.user_id,
            'user_name': request.user.user_name,
            'email': request.user.email,
            },
            status=status.HTTP_200_OK)


# ユーザ情報更新のView(PUT)
class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'user_name'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            if self.request.data['user_name'] == self.request.user.user_name and self.request.user.check_password(self.request.data['before_password']):
               # new_password = self.request.data['new_password']    #新しいパスワード
                instance = self.queryset.get(user_name=self.request.user)
                return instance #, new_password
            else:
#                raise PermissionDenied
                raise PermissionError
        except Account.DoesNotExist:
            raise Http404
 #       except KeyError:


"""
    def get_object(self):
        try:
            instance = self.queryset.get(user_name=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404
"""


# ユーザ削除のView(DELETE)
class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'user_name'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(user_name=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404

"""
#ログアウト
class SpaUserLogoutView(generics.RetrieveAPIView):    
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""