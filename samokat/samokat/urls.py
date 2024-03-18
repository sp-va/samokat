"""
URL configuration for samokat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

from products.views import GetProductsAPIView, AdminProductsAPIView
from .views import RootAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', GetProductsAPIView.as_view(), name="Список всех продуктов"),

    path('products/manage/', AdminProductsAPIView.as_view(), name="Добавить новый продукт"),
    path('products/manage/<uuid:id>/', AdminProductsAPIView.as_view(), name="Добавить новый продукт"),

    path('', RootAPIView.as_view(), name='redirect from root to auth'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
