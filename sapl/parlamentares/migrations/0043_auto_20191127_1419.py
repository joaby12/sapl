# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-27 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0042_auto_20191126_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bancada',
            options={'ordering': ('-legislatura__numero', 'nome'), 'verbose_name': 'Bancada Parlamentar', 'verbose_name_plural': 'Bancadas Parlamentares'},
        ),
        migrations.AlterModelOptions(
            name='parlamentarbancada',
            options={'ordering': ('cargo', 'parlamentar__nome_parlamentar'), 'verbose_name': 'Parlamentar', 'verbose_name_plural': 'Parlamentares'},
        ),
    ]