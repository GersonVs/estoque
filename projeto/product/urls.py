from django.urls import path
from projeto.product import views as v

app_name='product'

urlpatterns=[
    path('', v.produto_list, name='produto_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),

]