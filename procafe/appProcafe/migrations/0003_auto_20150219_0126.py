# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150219_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 49, 506246), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 49, 504050), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 49, 504360), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 49, 497493), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
