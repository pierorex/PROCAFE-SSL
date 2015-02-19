# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0003_auto_20150219_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 19, 1, 27, 10, 53861)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 19, 1, 27, 10, 51668)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 19, 1, 27, 10, 51989)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 19, 1, 27, 10, 44885)),
            preserve_default=True,
        ),
    ]
