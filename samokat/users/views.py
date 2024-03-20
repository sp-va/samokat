from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer



class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer


