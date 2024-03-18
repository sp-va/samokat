import uuid

from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product


class GetProductsAPIView(generics.ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class AdminProductsAPIView(APIView):
    permission_classes = [IsAdminUser,]
    authentication_classes = [JWTAuthentication,]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: uuid.uuid4):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
