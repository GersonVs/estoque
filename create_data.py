import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.product.models import Produto

class Utils:
    #Essa classe gera números aleatórios dado um numero de digitos"
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits)for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto = produto,
                importado = choice((True, False)),
                codigo = Utils.gen_digits(8),
                preco = random()*randint(10,50),
                estoque = randint(10,200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)#o metodo bulk_create insere a lista de objetos fornecida no banco de dados 
 
produtos = (
    'Carne',
    'Leite',
    'Feijão',
    'Arroz',
    'Farinha',
    'Batata',
    'Tomate',
    'Pão',
    'Café', 
    'Banana',
    'Açúcar',
    'Óleo', 
    'Manteiga',
    'Sal',
    'Macarrão',
    'Peixe',
    'Creme dental',
    'Cerveja',
    'Refrigerante',
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

tac = timeit.default_timer()
 
print('tempo:|',tac - tic)