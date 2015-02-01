# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150201_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='sede',
            field=models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='sede',
            field=models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='sede',
            field=models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede'),
            preserve_default=True,
        ),
    ]
