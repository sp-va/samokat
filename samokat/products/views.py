import uuid

from django.core.exceptions import FieldError
from django.db.models import Q

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

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


class ProductsSearch(ListAPIView):
    def get(self, request):
        try:
            query = request.query_params.get("q")
            filter_str = Q(name__icontains=query)
            queryset = Product.objects.filter(filter_str).values("name", "id")
            serializer = ProductSerializer(data=queryset, many=True)
            return Response(serializer.initial_data)
        except ValueError:
            raise ValueError("Отсутствует строка q для фильтрации")


class SortedProducts(ListAPIView):
    def get(self, request):
        try:
            order_by = request.query_params.get("field")
            objects = Product.objects.order_by(order_by).values("id", "name", "description", "shelf_life", "manufacturer")
            serializer = ProductSerializer(data=objects, many=True)
            return Response(serializer.initial_data)
        except FieldError:
            raise FieldError("Отсутствует строка field для фильтрации")






