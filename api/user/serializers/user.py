from rest_framework import serializers
from apps.user.models import Account
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Account
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'gender'
        ]