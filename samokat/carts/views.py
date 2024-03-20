from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsAdminOrOwner
from .serializers import OrderCartSerializer
from .models import OrderCart
from users.models import User



class CartsAPIView(APIView):
    # authentication_classes = [JWTAuthentication,]
    # permission_classes = [IsAdminOrOwner,]
    def get(self, request):
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

        order_cart.products.add(*products)
        dict_model = model_to_dict(order_cart)
        serializer = OrderCartSerializer(data=dict_model)

        if serializer.is_valid():
            # owner = User.objects.get(email=serializer.data["owner"])
            # cart_object = OrderCart.objects.get_or_create(owner=owner)
            # cart_object.save()
            serializer.save()

            # if not cart_object:
            #     create_cart = OrderCart.objects.create(owner=owner)
            #     create_cart.save()
            return Response(serializer.data)
        return Response(serializer.errors)
