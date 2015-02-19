# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0003_auto_20150218_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 4, 26, 56369), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 4, 26, 53369), verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 4, 26, 54368), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 4, 26, 48368), verbose_name='Fecha de Nacimiento'),
        ),
    ]
