# Generated by Django 3.0.8 on 2020-07-05 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200705_0153'),
        ('estoque', '0002_auto_20200705_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoqueitens',
            name='produto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.Produto'),
            preserve_default=False,
        ),
    ]