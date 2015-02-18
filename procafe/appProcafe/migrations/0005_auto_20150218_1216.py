# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0004_auto_20150217_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userapplication',
            name='is_pending',
        ),
        migrations.AddField(
            model_name='userapplication',
            name='status',
            field=models.CharField(verbose_name='Estado de la Solicitud', choices=[('PENDIENTE', 'Pendiente'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], max_length=20, default='PENDIENTE'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 12, 16, 38, 818292)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 12, 16, 38, 816292)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 12, 16, 38, 816571)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 12, 16, 38, 809065)),
            preserve_default=True,
        ),
    ]
