# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0008_auto_20150217_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 17, 57, 32, 932092), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
