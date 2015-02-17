# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(serialize=False, max_length=200, verbose_name='Nombre', primary_key=True, default=None)),
                ('description', models.CharField(verbose_name='Descripción', max_length=200, default=None)),
                ('content', models.CharField(verbose_name='Contenido', max_length=200, default=None)),
                ('video_url', models.URLField(verbose_name='URL del video', max_length=1000, default=None)),
                ('modality', models.CharField(choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')], verbose_name='Modalidad', max_length=200, default='PRESENCIAL')),
                ('instructor', models.CharField(verbose_name='Instructor', max_length=200, default=None)),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Lugar', max_length=200, default='SARTENEJAS')),
                ('number_hours', models.IntegerField(verbose_name='Número de Horas')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'verbose_name': 'Curso',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede', max_length=10, default='SARTENEJAS')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
                'verbose_name': 'Departamento',
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
                'verbose_name': 'Documento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Cargo', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Cargos',
                'verbose_name': 'Cargo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RemoveRequest',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('firstname', models.CharField(verbose_name='Nombre', max_length=50, default='')),
                ('lastname', models.CharField(verbose_name='Apellido', max_length=50, default='')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=200, default=None)),
                ('request_type', models.CharField(choices=[('INSCRIPCION', 'Inscripción'), ('RETIRO', 'Retiro')], verbose_name='Tipo de Solicitud', max_length=12, default=None)),
                ('request_date', models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 1, 26, 48, 927496))),
                ('is_pending', models.BooleanField(verbose_name='Aprobación Pendiente', default=1)),
                ('course_ID', models.ForeignKey(verbose_name='Curso', to='appProcafe.Course', default=None)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes de Cursos',
                'verbose_name': 'Solicitud de Cursos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Riesgo', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Riesgos',
                'verbose_name': 'Riesgo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede', max_length=10, default='SARTENEJAS')),
                ('department_ID', models.ForeignKey(verbose_name='Dpto', to='appProcafe.Department', default=True)),
            ],
            options={
                'verbose_name_plural': 'Secciones',
                'verbose_name': 'Sección',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('term', models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], verbose_name='Trimestre', max_length=200, default='SEP-DIC')),
                ('year', models.IntegerField(verbose_name='Año', max_length=4)),
                ('status', models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], verbose_name='Estado', max_length=200, default=None)),
                ('course_ID', models.ForeignKey(verbose_name='Curso', to='appProcafe.Course', default=None)),
            ],
            options={
                'verbose_name_plural': 'Cursa',
                'verbose_name': 'Cursa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.CharField(validators=[django.core.validators.RegexValidator(code='invalid_phone', message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', regex='^[0-9]{4}-[0-9]{7}$')], verbose_name='Número (xxxx-xxxxxxx)', max_length=12, default=None)),
            ],
            options={
                'verbose_name_plural': 'Teléfonos',
                'verbose_name': 'Teléfono',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Unidad de Adscripción', max_length=200, default=None)),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede', max_length=10, default='SARTENEJAS')),
            ],
            options={
                'verbose_name_plural': 'Unidades',
                'verbose_name': 'Unidad',
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
            name='UserApplication',
            fields=[
                ('ID_number', models.IntegerField(serialize=False, verbose_name='Cédula', primary_key=True, default=0)),
                ('USB_ID', models.CharField(null=True, validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')], unique=True, max_length=8)),
                ('firstname', models.CharField(verbose_name='Nombre', max_length=50, default='')),
                ('lastname', models.CharField(verbose_name='Apellido', max_length=50, default='')),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 1, 26, 48, 926451))),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], verbose_name='Tipo de Nómina', max_length=14, default=None)),
                ('type', models.CharField(choices=[('----', '----')], verbose_name='Tipo de Personal', max_length=20, default=None)),
                ('location', models.CharField(verbose_name='Ubicación de Trabajo', max_length=200, default=None)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=200, default=None)),
                ('request_date', models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 1, 26, 48, 926619))),
                ('is_pending', models.BooleanField(verbose_name='Aprobación Pendiente', default=1)),
                ('position', models.ForeignKey(verbose_name='Cargo', to='appProcafe.Position', default=None)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes de Registro',
                'verbose_name': 'Solicitud de Registro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ID_number', models.IntegerField(serialize=False, verbose_name='Cédula', primary_key=True, default=0)),
                ('USB_ID', models.CharField(null=True, validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')], unique=True, max_length=8)),
                ('firstname', models.CharField(verbose_name='Nombre', max_length=50, default='')),
                ('lastname', models.CharField(verbose_name='Apellido', max_length=50, default='')),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 1, 26, 48, 922058))),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], verbose_name='Tipo de Nómina', max_length=14, default=None)),
                ('type', models.CharField(choices=[('----', '----')], verbose_name='Tipo de Personal', max_length=20, default=None)),
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
        migrations.AddField(
            model_name='removerequest',
            name='USB_ID',
            field=models.ForeignKey(validators=[django.core.validators.RegexValidator(code='invalid_usbid', message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$')], to='appProcafe.UserProfile', to_field='USB_ID', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='ID_number',
            field=models.ForeignKey(verbose_name='Cédula', to='appProcafe.UserProfile', default=0),
            preserve_default=True,
        ),
    ]
