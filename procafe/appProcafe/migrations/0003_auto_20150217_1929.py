# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150217_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 19, 29, 20, 223092), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 19, 29, 20, 220828), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 19, 29, 20, 221213), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 19, 29, 20, 188052), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
