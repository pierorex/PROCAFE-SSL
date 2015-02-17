# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0003_auto_20150217_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 29, 55, 752470)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 29, 55, 750669)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 29, 55, 750944)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 29, 55, 742951)),
            preserve_default=True,
        ),
    ]
