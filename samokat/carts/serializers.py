from rest_framework import serializers

from .models import OrderCart
from products.models import Product


class OrderCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCart
        fields = "__all__"