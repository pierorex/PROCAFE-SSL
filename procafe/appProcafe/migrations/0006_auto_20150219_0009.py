# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0005_auto_20150218_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 19, 0, 9, 49, 865036)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 19, 0, 9, 49, 863666)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 19, 0, 9, 49, 863846)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 19, 0, 9, 49, 860090)),
            preserve_default=True,
        ),
    ]
