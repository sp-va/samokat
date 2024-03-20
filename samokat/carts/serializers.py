from rest_framework import serializers

from .models import OrderCart
from products.models import Product


class OrderCartSerializer(serializers.ModelSerializer):
    # queryset = Product.objects.all()
    # products = serializers.PrimaryKeyRelatedField(queryset=queryset, allow_null=True)
    class Meta:
        model = OrderCart
        fields = "__all__"