from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm

def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)

def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)

def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)

class ProdutoCreate(CreateView): #https://ccbv.co.uk/ CreateView cria um novo objeto, com uma resposta renderizada por um model. Dessa forma não preciso me preocupar com a maneira de criar as coisas.
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView): 
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

def produto_delete(request, pk): 
   produto = Produto.objects.get(pk=pk)
   produto.delete()
   obj=Produto.objects.all()
   context={'object_list': obj}
   return render(request, 'produto_list.html', context)
