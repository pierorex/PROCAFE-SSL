# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 15, 18, 14, 851309), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 15, 18, 14, 849293), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 15, 18, 14, 849579), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 15, 18, 14, 841979), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
