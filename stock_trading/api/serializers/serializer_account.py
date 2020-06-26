from rest_framework import serializers


class AccountResponseSerializer(serializers.Serializer):
    account_number = serializers.CharField()