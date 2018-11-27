from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from rest_framework import permissions, status, viewsets
from .models import Account, AccountManager


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('user_name', 'email', 'password')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            # instance = super().update(instance, validated_data)
            instance.user_name = validated_data['user_name']
            instance.email = validated_data['email']
        instance.save()
        return instance
