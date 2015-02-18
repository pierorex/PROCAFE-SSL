# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(serialize=False, default=None, max_length=200, verbose_name='Nombre', primary_key=True)),
                ('description', models.CharField(default=None, max_length=200, verbose_name='Descripción')),
                ('content', models.CharField(default=None, max_length=200, verbose_name='Contenido')),
                ('video_url', models.URLField(default=None, max_length=1000, verbose_name='URL del video')),
                ('modality', models.CharField(default='PRESENCIAL', max_length=200, choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')], verbose_name='Modalidad')),
                ('instructor', models.CharField(default=None, max_length=200, verbose_name='Instructor')),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(default='SARTENEJAS', max_length=200, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Lugar')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Cargo')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(default=None, max_length=200, verbose_name='E-mail')),
                ('request_type', models.CharField(default=None, max_length=12, choices=[('INSCRIPCION', 'Inscripción'), ('RETIRO', 'Retiro')], verbose_name='Tipo de Solicitud')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 15, 12, 2, 718171), verbose_name='Fecha de la Solicitud')),
                ('is_pending', models.BooleanField(default=1, verbose_name='Aprobación Pendiente')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Riesgo')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede')),
                ('department_ID', models.ForeignKey(default=True, verbose_name='Dpto', to='appProcafe.Department')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('term', models.CharField(default='SEP-DIC', max_length=200, choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], verbose_name='Trimestre')),
                ('year', models.IntegerField(max_length=4, verbose_name='Año')),
                ('status', models.CharField(default=None, max_length=200, choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], verbose_name='Estado')),
                ('course_ID', models.ForeignKey(default=None, verbose_name='Curso', to='appProcafe.Course')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('number', models.CharField(default=None, max_length=12, verbose_name='Número (xxxx-xxxxxxx)', validators=[django.core.validators.RegexValidator(message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', regex='^[0-9]{4}-[0-9]{7}$', code='invalid_phone')])),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='Unidad de Adscripción')),
                ('sede', models.CharField(default='SARTENEJAS', max_length=10, choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], verbose_name='Sede')),
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
                ('ID_number', models.IntegerField(serialize=False, default=0, verbose_name='Cédula', primary_key=True)),
                ('USB_ID', models.CharField(max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$', code='invalid_usbid')])),
                ('first_name', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 15, 12, 2, 716137), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(default=None, max_length=14, choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], verbose_name='Tipo de Nómina')),
                ('type', models.CharField(default=None, max_length=20, choices=[('----', '----')], verbose_name='Tipo de Personal')),
                ('location', models.CharField(default=None, max_length=200, verbose_name='Ubicación de Trabajo')),
                ('email', models.EmailField(default=None, max_length=200, verbose_name='E-mail')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 15, 12, 2, 716420), verbose_name='Fecha de la Solicitud')),
                ('status', models.CharField(default='PENDIENTE', max_length=20, choices=[('PENDIENTE', 'Pendiente'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], verbose_name='Estado de la Solicitud')),
                ('position', models.ForeignKey(default=None, verbose_name='Cargo', to='appProcafe.Position')),
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
                ('ID_number', models.IntegerField(serialize=False, default=0, verbose_name='Cédula', primary_key=True)),
                ('USB_ID', models.CharField(max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$', code='invalid_usbid')])),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 15, 12, 2, 709008), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(default=None, max_length=14, choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], verbose_name='Tipo de Nómina')),
                ('type', models.CharField(default=None, max_length=20, choices=[('----', '----')], verbose_name='Tipo de Personal')),
                ('location', models.CharField(default=None, max_length=200, verbose_name='Ubicación de Trabajo')),
                ('finished_hours', models.IntegerField(default=0, verbose_name='Horas finalizadas')),
                ('position', models.ForeignKey(default=None, verbose_name='Cargo', to='appProcafe.Position')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telephone',
            name='user_ID',
            field=models.ForeignKey(default=0, verbose_name='Cédula del Trabajador', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(default=None, verbose_name='Nombre', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='ID_number',
            field=models.ForeignKey(default=0, verbose_name='Cédula', related_name='ID_number_remove_reques', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='USB_ID',
            field=models.ForeignKey(default=None, related_name='USB_ID_remove_reques', validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', regex='^[0-9]{2}-[0-9]{5}$', code='invalid_usbid')], to_field='USB_ID', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='course_ID',
            field=models.ForeignKey(default=None, verbose_name='Curso', to='appProcafe.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(default=None, verbose_name='Unidad', to='appProcafe.Unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(default=None, verbose_name='Dpto', to='appProcafe.Department'),
            preserve_default=True,
        ),
    ]
