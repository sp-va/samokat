from rest_framework.views import APIView
from django.shortcuts import redirect


class RootAPIView(APIView):
     def get(self, request):
         return redirect("auth/token")
