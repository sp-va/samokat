from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.core.exceptions import PermissionDenied

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsAdminOrOwner
from .serializers import OrderCartSerializer
from .models import OrderCart
from users.models import User



class CartsAPIView(APIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAdminOrOwner,]
    def get(self, request):
        if not request.user.is_superuser:
            raise PermissionDenied
        query = OrderCart.objects.all()
        serializer = OrderCartSerializer(query, many=True)
        return Response(serializer.data)
    def post(self, request):
        owner_email = request.data['owner']
        products = request.data['products']

        try:
            order_cart = OrderCart.objects.get(owner__email=owner_email)
        except:
            owner = User.objects.get(email=owner_email)
            order_cart = OrderCart.objects.create(owner=owner)

        self.check_object_permissions(request, order_cart)
        order_cart.products.add(*products)
        dict_model = model_to_dict(order_cart)
        serializer = OrderCartSerializer(data=dict_model)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) # Здесь при добавлении товара в корзину возвращается ошибка с неверным
                                            # форматом UUID, но при этом все нормально добавляется в БД
