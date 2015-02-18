# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150218_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 15, 18, 22, 97738)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 15, 18, 22, 95624)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 15, 18, 22, 95927)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 15, 18, 22, 88256)),
            preserve_default=True,
        ),
    ]
