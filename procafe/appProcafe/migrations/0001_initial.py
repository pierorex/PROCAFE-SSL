# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.CharField(default=None, max_length=200, verbose_name='Descripcion')),
                ('video_url', models.CharField(max_length=1000, verbose_name='URL del video')),
                ('type', models.CharField(choices=[('PRESENCIAL', 'Presencial'), ('A DISTANCIA', 'A distancia')], max_length=200, verbose_name='Tipo')),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=200, verbose_name='Lugar')),
                ('number_hours', models.IntegerField(verbose_name='Número de Horas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del Depto.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Cargo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Riesgo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre de la Sección')),
                ('department_ID', models.ForeignKey(to='appProcafe.Department', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('term', models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], max_length=200)),
                ('year', models.IntegerField(max_length=4, verbose_name='Año')),
                ('status', models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], max_length=200)),
                ('course_ID', models.ForeignKey(to='appProcafe.Course', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Unidad de Adscripción')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ID_number', models.IntegerField(primary_key=True, default=0, verbose_name='Cédula', serialize=False)),
                ('type', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], max_length=200)),
                ('finished_hours', models.IntegerField(default=0, verbose_name='Horas finalizadas')),
                ('status', models.CharField(max_length=200, verbose_name='Estado')),
                ('is_enabled', models.BooleanField(default=1, verbose_name='Habilitado')),
                ('position', models.ForeignKey(default=0, verbose_name='Cargo', to='appProcafe.Position')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(to='appProcafe.UserProfile', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(to='appProcafe.Unit', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(to='appProcafe.Department'),
            preserve_default=True,
        ),
    ]
