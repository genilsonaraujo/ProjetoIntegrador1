# Generated by Django 5.1.6 on 2025-03-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegradors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo_barras',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
