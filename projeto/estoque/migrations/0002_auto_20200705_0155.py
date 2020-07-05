# Generated by Django 3.0.8 on 2020-07-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoqueitens',
            name='produto',
        ),
        migrations.AlterField(
            model_name='estoque',
            name='atividade',
            field=models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1),
        ),
    ]
