from django.db import models

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    codigo = models.CharField('Código', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=9, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)

    class Meta:
        ordering=('produto',)

    def __str__(self):
        return self.produto


