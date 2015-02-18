# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(default=None, max_length=200, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('description', models.CharField(default=None, max_length=200, verbose_name='Descripción')),
                ('content', models.CharField(default=None, max_length=200, verbose_name='Contenido')),
                ('video_url', models.URLField(default=None, max_length=1000, verbose_name='URL del video')),
                ('modality', models.CharField(choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')], default='PRESENCIAL', max_length=200, verbose_name='Modalidad')),
                ('instructor', models.CharField(default=None, max_length=200, verbose_name='Instructor')),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=200, verbose_name='Lugar')),
                ('number_hours', models.IntegerField(verbose_name='Número de Horas')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='RemoveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(default=None, max_length=200, verbose_name='E-mail')),
                ('request_type', models.CharField(choices=[('INSCRIPCION', 'Inscripción'), ('RETIRO', 'Retiro')], default=None, max_length=12, verbose_name='Tipo de Solicitud')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 10, 19, 49, 381918), verbose_name='Fecha de la Solicitud')),
                ('is_pending', models.BooleanField(default=1, verbose_name='Aprobación Pendiente')),
            ],
            options={
                'verbose_name': 'Solicitud de Cursos',
                'verbose_name_plural': 'Solicitudes de Cursos',
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Riesgo')),
            ],
            options={
                'verbose_name': 'Riesgo',
                'verbose_name_plural': 'Riesgos',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede')),
                ('department_ID', models.ForeignKey(default=True, to='appProcafe.Department', verbose_name='Dpto')),
            ],
            options={
                'verbose_name': 'Sección',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], default='SEP-DIC', max_length=200, verbose_name='Trimestre')),
                ('year', models.IntegerField(max_length=4, verbose_name='Año')),
                ('status', models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], default=None, max_length=200, verbose_name='Estado')),
                ('course_ID', models.ForeignKey(default=None, to='appProcafe.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Cursa',
                'verbose_name_plural': 'Cursa',
            },
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default=None, max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', regex='^[0-9]{4}-[0-9]{7}$')], verbose_name='Número (xxxx-xxxxxxx)')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='Unidad de Adscripción')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], default='SARTENEJAS', max_length=10, verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('ID_number', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Cédula')),
                ('USB_ID', models.CharField(max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')])),
                ('firstname', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 10, 19, 49, 380918), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], default=None, max_length=14, verbose_name='Tipo de Nómina')),
                ('type', models.CharField(choices=[('----', '----')], default=None, max_length=20, verbose_name='Tipo de Personal')),
                ('location', models.CharField(default=None, max_length=200, verbose_name='Ubicación de Trabajo')),
                ('email', models.EmailField(default=None, max_length=200, verbose_name='E-mail')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 10, 19, 49, 380918), verbose_name='Fecha de la Solicitud')),
                ('status', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], default='PENDIENTE', max_length=20, verbose_name='Estado de la Solicitud')),
                ('position', models.ForeignKey(default=None, to='appProcafe.Position', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Solicitud de Registro',
                'verbose_name_plural': 'Solicitudes de Registro',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ID_number', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Cédula')),
                ('USB_ID', models.CharField(max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')])),
                ('firstname', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 10, 19, 49, 375917), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], default=None, max_length=14, verbose_name='Tipo de Nómina')),
                ('type', models.CharField(choices=[('----', '----')], default=None, max_length=20, verbose_name='Tipo de Personal')),
                ('location', models.CharField(default=None, max_length=200, verbose_name='Ubicación de Trabajo')),
                ('finished_hours', models.IntegerField(default=0, verbose_name='Horas finalizadas')),
                ('is_enabled', models.BooleanField(default=1, verbose_name='Habilitado')),
                ('position', models.ForeignKey(default=None, to='appProcafe.Position', verbose_name='Cargo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='telephone',
            name='user_ID',
            field=models.ForeignKey(default=0, to='appProcafe.UserProfile', verbose_name='Cédula del Trabajador'),
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(default=None, to='appProcafe.UserProfile', verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='removerequest',
            name='ID_number',
            field=models.ForeignKey(default=0, related_name='ID_number_remove_reques', to='appProcafe.UserProfile', verbose_name='Cédula'),
        ),
        migrations.AddField(
            model_name='removerequest',
            name='USB_ID',
            field=models.ForeignKey(default=None, related_name='USB_ID_remove_reques', to='appProcafe.UserProfile', to_field='USB_ID', validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')]),
        ),
        migrations.AddField(
            model_name='removerequest',
            name='course_ID',
            field=models.ForeignKey(default=None, to='appProcafe.Course', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(default=None, to='appProcafe.Unit', verbose_name='Unidad'),
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(default=None, to='appProcafe.Department', verbose_name='Dpto'),
        ),
    ]
