from rest_framework import serializers


class StockDataResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.CharField()
    volume = serializers.CharField()