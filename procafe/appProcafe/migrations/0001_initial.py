# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(verbose_name='Nombre', default=None, primary_key=True, max_length=200, serialize=False)),
                ('description', models.CharField(verbose_name='Descripción', default=None, max_length=200)),
                ('content', models.CharField(verbose_name='Contenido', default=None, max_length=200)),
                ('video_url', models.URLField(verbose_name='URL del video', default=None, max_length=1000)),
                ('modality', models.CharField(verbose_name='Modalidad', default='PRESENCIAL', max_length=200, choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')])),
                ('instructor', models.CharField(verbose_name='Instructor', default=None, max_length=200)),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(verbose_name='Lugar', default='SARTENEJAS', max_length=200, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')])),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(verbose_name='Sede', default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')])),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Cargo', max_length=200)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RemoveRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(verbose_name='Nombre', default='', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellido', default='', max_length=50)),
                ('email', models.EmailField(verbose_name='E-mail', default=None, max_length=200)),
                ('request_type', models.CharField(verbose_name='Tipo de Solicitud', default=None, max_length=12, choices=[('INSCRIPCION', 'Inscripción'), ('RETIRO', 'Retiro')])),
                ('request_date', models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 28, 0, 847618))),
                ('is_pending', models.BooleanField(verbose_name='Aprobación Pendiente', default=1)),
            ],
            options={
                'verbose_name': 'Solicitud de Cursos',
                'verbose_name_plural': 'Solicitudes de Cursos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=200)),
                ('sede', models.CharField(verbose_name='Sede', default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')])),
                ('department_ID', models.ForeignKey(verbose_name='Dpto', default=True, to='appProcafe.Department')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.CharField(verbose_name='Trimestre', default='SEP-DIC', max_length=200, choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')])),
                ('year', models.IntegerField(verbose_name='Año', max_length=4)),
                ('status', models.CharField(verbose_name='Estado', default=None, max_length=200, choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')])),
                ('course_ID', models.ForeignKey(verbose_name='Curso', default=None, to='appProcafe.Course')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(verbose_name='Número (xxxx-xxxxxxx)', default=None, validators=[django.core.validators.RegexValidator(message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', code='invalid_phone', regex='^[0-9]{4}-[0-9]{7}$')], max_length=12)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Unidad de Adscripción', default=None, max_length=200)),
                ('sede', models.CharField(verbose_name='Sede', default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')])),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('ID_number', models.IntegerField(verbose_name='Cédula', default=0, primary_key=True, serialize=False)),
                ('USB_ID', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], null=True)),
                ('firstname', models.CharField(verbose_name='Nombre', default='', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellido', default='', max_length=50)),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 28, 0, 845685))),
                ('paysheet', models.CharField(verbose_name='Tipo de Nómina', default=None, max_length=14, choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')])),
                ('type', models.CharField(verbose_name='Tipo de Personal', default=None, max_length=20, choices=[('----', '----')])),
                ('location', models.CharField(verbose_name='Ubicación de Trabajo', default=None, max_length=200)),
                ('email', models.EmailField(verbose_name='E-mail', default=None, max_length=200)),
                ('request_date', models.DateField(verbose_name='Fecha de la Solicitud', default=datetime.datetime(2015, 2, 17, 19, 28, 0, 845964))),
                ('is_pending', models.BooleanField(verbose_name='Aprobación Pendiente', default=1)),
                ('position', models.ForeignKey(verbose_name='Cargo', default=None, to='appProcafe.Position')),
            ],
            options={
                'verbose_name': 'Solicitud de Registro',
                'verbose_name_plural': 'Solicitudes de Registro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ID_number', models.IntegerField(verbose_name='Cédula', default=0, primary_key=True, serialize=False)),
                ('USB_ID', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], null=True)),
                ('firstname', models.CharField(verbose_name='Nombre', default='', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellido', default='', max_length=50)),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.datetime(2015, 2, 17, 19, 28, 0, 838044))),
                ('paysheet', models.CharField(verbose_name='Tipo de Nómina', default=None, max_length=14, choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')])),
                ('type', models.CharField(verbose_name='Tipo de Personal', default=None, max_length=20, choices=[('----', '----')])),
                ('location', models.CharField(verbose_name='Ubicación de Trabajo', default=None, max_length=200)),
                ('email', models.EmailField(verbose_name='E-mail', default=None, max_length=75)),
                ('finished_hours', models.IntegerField(verbose_name='Horas finalizadas', default=0)),
                ('is_enabled', models.BooleanField(verbose_name='Habilitado', default=1)),
                ('position', models.ForeignKey(verbose_name='Cargo', default=None, to='appProcafe.Position')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telephone',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Cédula del Trabajador', default=0, to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Nombre', default=None, to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='ID_number',
            field=models.ForeignKey(verbose_name='Cédula', default=0, related_name='ID_number_remove_reques', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='USB_ID',
            field=models.ForeignKey(default=None, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], related_name='USB_ID_remove_reques', to='appProcafe.UserProfile', to_field='USB_ID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='course_ID',
            field=models.ForeignKey(verbose_name='Curso', default=None, to='appProcafe.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(verbose_name='Unidad', default=None, to='appProcafe.Unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Dpto', default=None, to='appProcafe.Department'),
            preserve_default=True,
        ),
    ]
