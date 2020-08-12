"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import include, url
from projeto.product.views import ProdutoListApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoListApi)

urlpatterns = [
    path('api/'         ,include(router.urls)),
    path(''             , include('projeto.core.urls')),
    path('produto/'     , include('projeto.product.urls')),
    path('admin/'       , admin.site.urls),
    path('accounts/'    , include('projeto.accounts.urls')),
    path('accounts/'    , include('django.contrib.auth.urls')),
    path('chat/'        , include('projeto.estoque.urls')),
]
