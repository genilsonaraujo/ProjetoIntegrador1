# Generated by Django 4.2.10 on 2024-10-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegradors', '0012_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='endereco',
            field=models.CharField(default='Endereço Padrão', max_length=255),
        ),
    ]
