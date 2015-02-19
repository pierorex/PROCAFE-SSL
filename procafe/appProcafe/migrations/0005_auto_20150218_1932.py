# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0004_auto_20150218_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paysheet',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Tipo de Nómina'),
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 32, 56, 988229), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Tipo de Personal'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 32, 56, 987229), verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='paysheet',
            field=models.ForeignKey(default=None, to='appProcafe.Paysheet', verbose_name='Tipo de Nómina'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 32, 56, 987229), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='type',
            field=models.ForeignKey(default=None, to='appProcafe.Type', verbose_name='Tipo de Personal'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 19, 32, 56, 981228), verbose_name='Fecha de Nacimiento'),
        ),
    ]
