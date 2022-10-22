from rest_framework import serializers
from .models import Article_details


class CartItemSerializer(serializers.ModelSerializer):
    Title = serializers.CharField(max_length=200)
    Author = serializers.CharField(max_length=200)
    Publish_date = serializers.CharField(max_length=200)

    class Meta:
        model = Article_details
        fields = ('__all__')
