# Generated by Django 5.1.3 on 2024-11-10 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0003_rename_data_criacao_comentario_criado_em_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocolo', models.CharField(max_length=20, unique=True)),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('detalhes', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
