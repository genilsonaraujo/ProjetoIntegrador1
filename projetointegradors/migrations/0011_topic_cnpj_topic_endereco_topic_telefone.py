# Generated by Django 4.2.10 on 2024-05-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegradors', '0010_itemsaida_preco_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='cnpj',
            field=models.CharField(default='00.000.000/0000-00', max_length=20),
        ),
        migrations.AddField(
            model_name='topic',
            name='endereco',
            field=models.CharField(default='Endereço Padrão', max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='telefone',
            field=models.CharField(default='(00) 0000-0000', max_length=10),
        ),
    ]