# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-04-17 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0020_auto_20180416_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientemateria',
            name='sessao_plenaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessao.SessaoPlenaria'),
        ),
        migrations.AlterField(
            model_name='ordemdia',
            name='sessao_plenaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessao.SessaoPlenaria'),
        ),
    ]
