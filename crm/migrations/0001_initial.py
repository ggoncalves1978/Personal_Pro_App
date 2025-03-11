# Generated by Django 5.1.6 on 2025-02-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=45)),
                ('pais', models.CharField(max_length=45)),
                ('data_do_contato', models.DateField()),
                ('dia_da_semana', models.CharField(max_length=45)),
                ('canal', models.CharField(max_length=45)),
                ('data_de_fechamento', models.DateField()),
                ('follow_up', models.CharField(max_length=3)),
                ('chegou_na_oferta', models.CharField(max_length=45)),
                ('plano_escolhido', models.CharField(max_length=45)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
