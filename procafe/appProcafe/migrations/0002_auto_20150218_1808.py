# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapplication',
            name='sex',
            field=models.CharField(default='', max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 8, 53, 954783), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 8, 53, 953783), verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 8, 53, 953783), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 8, 53, 948782), verbose_name='Fecha de Nacimiento'),
        ),
    ]
