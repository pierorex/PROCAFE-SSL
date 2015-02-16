# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('ID_number', models.IntegerField(verbose_name='Cédula', default=0, primary_key=True, serialize=False)),
                ('USB_ID', models.CharField(validators=[django.core.validators.RegexValidator(code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$', message='El USB-ID debe ser de la forma xx-xxxxx.')], null=True, unique=True, max_length=8)),
                ('firstname', models.CharField(verbose_name='Nombre', default='', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellido', default='', max_length=50)),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 16, 18, 10, 32, 182425))),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], verbose_name='Tipo de Nómina', default=None, max_length=14)),
                ('type', models.CharField(choices=[('----', '----')], verbose_name='Tipo de Personal', default=None, max_length=20)),
                ('location', models.CharField(verbose_name='Ubicación de Trabajo', default=None, max_length=200)),
                ('email', models.EmailField(verbose_name='E-mail', default=None, max_length=75)),
                ('is_pending', models.BooleanField(verbose_name='Aprobación Pendiente', default=1)),
                ('position', models.ForeignKey(to='appProcafe.Position', default=None, verbose_name='Cargo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 16, 18, 10, 32, 182425)),
            preserve_default=True,
        ),
    ]
