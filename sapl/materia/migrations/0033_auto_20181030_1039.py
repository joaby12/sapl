# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-30 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0032_auto_20181022_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposicao',
            name='cancelado',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Cancelada ?'),
        ),
        migrations.AddField(
            model_name='proposicao',
            name='observacao',
            field=models.TextField(blank=True, verbose_name='Observação'),
        ),
    ]
