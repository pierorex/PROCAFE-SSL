# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0004_auto_20150206_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 6, 4, 10, 12, 1064), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
