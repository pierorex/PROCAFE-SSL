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
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 28, 53, 175317)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 28, 53, 173476)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 28, 53, 173796)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 28, 53, 165434)),
            preserve_default=True,
        ),
    ]
