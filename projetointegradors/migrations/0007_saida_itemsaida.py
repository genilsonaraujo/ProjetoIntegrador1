# Generated by Django 4.2.10 on 2024-04-19 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegradors', '0006_delete_listasaida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField(auto_now_add=True)),
                ('observacao', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSaida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetointegradors.produto')),
                ('saida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='projetointegradors.saida')),
            ],
        ),
    ]
