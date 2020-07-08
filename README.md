# Estoque
Aplicação de controle de estoque

## Como rodar o projeto: 

- Clone esse repositório.
- Crie uma virtualenv.
- Ative o virtualenv.
- Instale as dependências.
- Crie o banco de dados.
- Crie um usuário para entrar no sistema.

```
git clone https://github.com/GersonVs/estoque.git
cd estoque
python -m venv .env
cd env/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Links úteis
[python-decouple](https://github.com/henriquebastos/python-decouple)

[Bootstrap Starter template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

[Classy Class-Based Views](https://ccbv.co.uk/)

[django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)

[The Django admin site](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)
