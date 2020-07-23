from django.db import models
from django.urls import reverse_lazy

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    codigo = models.CharField('Código', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=9, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)

    class Meta:
        permissions=(('pode_adicionar_produto', 'Pode adicionar produto'),)
        ordering=('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('product:produto_detail', kwargs={'pk': self.pk})
        

