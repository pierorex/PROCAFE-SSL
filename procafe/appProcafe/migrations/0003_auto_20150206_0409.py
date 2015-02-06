# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150201_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 6, 4, 9, 8, 79882)),
            preserve_default=True,
        ),
    ]
