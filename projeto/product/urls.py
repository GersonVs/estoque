from django.urls import path
from projeto.product import views as v

app_name='product'

urlpatterns=[
    path('', v.produto_list, name='produto_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', v.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/delete/', v.produto_delete, name='produto_delete'),
]