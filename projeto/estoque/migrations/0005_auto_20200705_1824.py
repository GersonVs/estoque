# Generated by Django 3.0.8 on 2020-07-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_auto_20200705_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='atividade',
            field=models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1),
        ),
    ]
