from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('projetointegradors', '0014_previous_migration_name'),  # Atualize para o número correto da última migração
    ]

    operations = [
        migrations.AddField(
            model_name='itemsaida',
            name='preco_unitario',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0),
        ),
    ]
