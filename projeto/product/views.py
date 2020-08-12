from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets
from .serializers import ProdutoSerializer
from .models import Produto
from .forms import ProdutoForm

class ProdutoList(LoginRequiredMixin,ListView):
    model = Produto
    queryset = Produto.objects.all()
    template_name = 'produto_list.html'

@login_required

def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)

class ProdutoCreate(LoginRequiredMixin,CreateView): #https://ccbv.co.uk/ CreateView cria um novo objeto, com uma resposta renderizada por um model. Dessa forma não preciso me preocupar com a maneira de criar as coisas.
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(LoginRequiredMixin,UpdateView): 
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

@login_required
def produto_delete(request, pk): 
   obj=Produto.objects.all()
   context={'object_list': obj}
   produto = Produto.objects.get(pk=pk)
   produto.delete()
   return render(request, 'produto_list.html', context)

class ProdutoListApi(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

