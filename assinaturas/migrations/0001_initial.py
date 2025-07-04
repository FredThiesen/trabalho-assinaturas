# Generated by Django 4.2 on 2025-06-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('mensalidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('clientes', models.ManyToManyField(to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
    ]
