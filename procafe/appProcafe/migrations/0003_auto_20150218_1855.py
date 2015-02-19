# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0002_auto_20150218_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paysheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Tipo de Nómina')),
            ],
            options={
                'verbose_name': 'Tipo de Nómina',
                'verbose_name_plural': 'Tipos de Nómina',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Tipo de Personal')),
            ],
            options={
                'verbose_name': 'Tipo de Personal',
                'verbose_name_plural': 'Tipos de Personal',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='sex',
            field=models.CharField(default='', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 55, 54, 544111), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 55, 54, 543112), verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 55, 54, 543112), verbose_name='Fecha de la Solicitud'),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='sex',
            field=models.CharField(default='', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 18, 55, 54, 538111), verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='paysheet',
            field=models.ForeignKey(default=None, to='appProcafe.Paysheet', verbose_name='Tipo de Nómina'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.ForeignKey(default=None, to='appProcafe.Type', verbose_name='Tipo de Personal'),
        ),
    ]
