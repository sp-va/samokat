from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import UserManager
from .serializers import UserSerializer
from carts.models import OrderCart


class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer
    # def post(self, request):
    #     serializer_class = UserSerializer(data=request.data)
    #     serializer_class.is_valid(raise_exception=True)
    #     serializer_class.save()
    #     return Response({"new_user": serializer_class.data})

    def perform_create(self, serializer):
        return OrderCart.objects.create(owner=serializer.email)
