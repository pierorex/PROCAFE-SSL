# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150216_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 16, 18, 31, 39, 190989), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 2, 16, 18, 31, 39, 190989), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
