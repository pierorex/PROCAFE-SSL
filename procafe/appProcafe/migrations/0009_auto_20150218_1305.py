# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0008_auto_20150218_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 13, 5, 2, 561104), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 13, 5, 2, 558915), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 13, 5, 2, 559211), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 13, 5, 2, 551373), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
