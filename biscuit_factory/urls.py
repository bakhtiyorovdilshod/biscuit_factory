"""biscuit_factory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('api.user.urls')),
    path('api/v1/product/', include('api.product.urls')),
    path('api/v1/warehouse/', include('api.warehouse.urls')),
    path('api/v1/supplier/', include('api.supplier.urls')),
    path('api/v1/biscuit/', include('api.biscuit.urls')),
    path('api/v1/recipe/', include('api.recipe.urls')),
    path('api/v1/expense/', include('api.expense.urls')),
    path('api/v1/client/', include('api.client.urls')),
]
