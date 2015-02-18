# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150218_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userapplication',
            name='birthday',
        ),
        migrations.AddField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 18, 37, 42, 535554)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 18, 37, 42, 537533)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 18, 37, 42, 535837)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 18, 37, 42, 529168)),
            preserve_default=True,
        ),
    ]
