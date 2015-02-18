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
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Ubicación', unique=True, max_length=50)),
                ('risks', models.ManyToManyField(to='appProcafe.Risk')),
            ],
            options={
                'verbose_name': 'Ubicación',
                'verbose_name_plural': 'Ubicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='position',
            name='risks',
            field=models.ManyToManyField(to='appProcafe.Risk'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(verbose_name='Cargo', unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='removerequest',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 18, 13, 49, 347752)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 18, 13, 49, 345683)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='request_date',
            field=models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 18, 18, 13, 49, 345962)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 18, 18, 13, 49, 339286)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.ForeignKey(verbose_name='Ubicación', to='appProcafe.Location', default=None),
            preserve_default=True,
        ),
    ]
