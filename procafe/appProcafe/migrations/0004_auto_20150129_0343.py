# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0003_auto_20150128_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_hours',
            field=models.IntegerField(verbose_name='NAmero de Horas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='year',
            field=models.IntegerField(max_length=4, verbose_name='AAo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(max_length=200, choices=[('ACADEMICO', 'AcadAmico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')]),
            preserve_default=True,
        ),
    ]
