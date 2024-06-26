# Generated by Django 4.2.10 on 2024-04-05 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegradors', '0004_produto_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaSaida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data_saida', models.DateField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetointegradors.produto')),
            ],
        ),
    ]
