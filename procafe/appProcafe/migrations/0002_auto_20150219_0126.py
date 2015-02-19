# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paysheet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Tipo de Nómina')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Nómina',
                'verbose_name': 'Tipo de Nómina',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Tipo de Personal')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Personal',
                'verbose_name': 'Tipo de Personal',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='sex',
            field=models.CharField(default='', max_length=10, verbose_name='Sexo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userapplication',
            name='sex',
            field=models.CharField(default='', max_length=10, verbose_name='Sexo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 38, 542851), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='risk',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Riesgo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(default=None, max_length=200, unique=True, verbose_name='Unidad de Adscripción'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 38, 540628), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='paysheet',
            field=models.ForeignKey(to='appProcafe.Paysheet', verbose_name='Tipo de Nómina', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 38, 540980), verbose_name='Fecha de la Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='type',
            field=models.ForeignKey(to='appProcafe.Type', verbose_name='Tipo de Personal', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 1, 26, 38, 533988), verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='finished_hours',
            field=models.PositiveIntegerField(default=0, verbose_name='Horas finalizadas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='paysheet',
            field=models.ForeignKey(to='appProcafe.Paysheet', verbose_name='Tipo de Nómina', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.ForeignKey(to='appProcafe.Type', verbose_name='Tipo de Personal', default=None),
            preserve_default=True,
        ),
    ]
