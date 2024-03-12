from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


from products.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()