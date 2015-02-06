# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, verbose_name='Nombre', max_length=200, default=None)),
                ('description', models.CharField(verbose_name='Descripción', max_length=200, default=None)),
                ('content', models.CharField(verbose_name='Contenido', max_length=200, default=None)),
                ('video_url', models.URLField(verbose_name='URL del video', max_length=1000, default=None)),
                ('modality', models.CharField(max_length=200, verbose_name='Modalidad', choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')], default='PRESENCIAL')),
                ('instructor', models.CharField(verbose_name='Instructor', max_length=200, default=None)),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(max_length=200, verbose_name='Lugar', choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS')),
                ('number_hours', models.IntegerField(verbose_name='Número de Horas')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(max_length=10, verbose_name='Sede', choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Dpto', to='appProcafe.Department', default=None),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Cargo', max_length=200)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Riesgo', max_length=200)),
            ],
            options={
                'verbose_name': 'Riesgo',
                'verbose_name_plural': 'Riesgos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(max_length=10, verbose_name='Sede', choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS')),
                ('department_ID', models.ForeignKey(verbose_name='Dpto', to='appProcafe.Department', default=True)),
            ],
            options={
                'verbose_name': 'Sección',
                'verbose_name_plural': 'Secciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('term', models.CharField(max_length=200, verbose_name='Trimestre', choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], default='SEP-DIC')),
                ('year', models.IntegerField(verbose_name='Año', max_length=4)),
                ('status', models.CharField(max_length=200, verbose_name='Estado', choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], default=None)),
                ('course_ID', models.ForeignKey(verbose_name='Curso', to='appProcafe.Course', default=None)),
            ],
            options={
                'verbose_name': 'Cursa',
                'verbose_name_plural': 'Cursa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('number', models.CharField(verbose_name='Número (xxxx-xxxxxxx)', validators=[django.core.validators.RegexValidator(regex='^[0-9]{4}-[0-9]{7}$', message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', code='invalid_phone')], max_length=12, default=None)),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Unidad de Adscripción', max_length=200, default=None)),
                ('sede', models.CharField(max_length=10, verbose_name='Sede', choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(verbose_name='Unidad', to='appProcafe.Unit', default=None),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ID_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Cédula', default=0)),
                ('USB_ID', models.CharField(unique=True, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{2}-[0-9]{5}$', message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid')], max_length=8)),
                ('firstname', models.CharField(verbose_name='Nombre', max_length=50, default='')),
                ('lastname', models.CharField(verbose_name='Apellido', max_length=50, default='')),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 1, 23, 18, 11, 433124))),
                ('paysheet', models.CharField(max_length=14, verbose_name='Tipo de Nómina', choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], default=None)),
                ('type', models.CharField(max_length=20, verbose_name='Tipo de Personal', choices=[('----', '----')], default=None)),
                ('location', models.CharField(verbose_name='Ubicación de Trabajo', max_length=200, default=None)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=75, default=None)),
                ('finished_hours', models.IntegerField(verbose_name='Horas finalizadas', default=0)),
                ('is_enabled', models.BooleanField(verbose_name='Habilitado', default=1)),
                ('position', models.ForeignKey(verbose_name='Cargo', to='appProcafe.Position', default=None)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telephone',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Cédula del Trabajador', to='appProcafe.UserProfile', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Nombre', to='appProcafe.UserProfile', default=None),
            preserve_default=True,
        ),
    ]
