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
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, default=None, verbose_name='Nombre')),
                ('description', models.CharField(max_length=200, default=None, verbose_name='Descripción')),
                ('content', models.CharField(max_length=200, default=None, verbose_name='Contenido')),
                ('video_url', models.URLField(max_length=1000, default=None, verbose_name='URL del video')),
                ('modality', models.CharField(choices=[('PRESENCIAL', 'Presencial'), ('DISTANCIA', 'A distancia')], max_length=200, default='PRESENCIAL', verbose_name='Modalidad')),
                ('instructor', models.CharField(max_length=200, default=None, verbose_name='Instructor')),
                ('init_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('location', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=200, default='SARTENEJAS', verbose_name='Lugar')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=10, default='SARTENEJAS', verbose_name='Sede')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
                'verbose_name': 'Departamento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Cargo')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=50, default='', verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, default='', verbose_name='Apellido')),
                ('email', models.EmailField(max_length=200, default=None, verbose_name='E-mail')),
                ('request_type', models.CharField(choices=[('INSCRIPCION', 'Inscripción'), ('RETIRO', 'Retiro')], max_length=12, default=None, verbose_name='Tipo de Solicitud')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 16, 21, 0, 884458), verbose_name='Fecha de la Solicitud')),
                ('is_pending', models.BooleanField(default=1, verbose_name='Aprobación Pendiente')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Riesgo')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=10, default='SARTENEJAS', verbose_name='Sede')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('term', models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], max_length=200, default='SEP-DIC', verbose_name='Trimestre')),
                ('year', models.IntegerField(max_length=4, verbose_name='Año')),
                ('status', models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], max_length=200, default=None, verbose_name='Estado')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='El número telefónico debe ser de la forma xxxx-xxxxxxx.', code='invalid_phone', regex='^[0-9]{4}-[0-9]{7}$')], default=None, verbose_name='Número (xxxx-xxxxxxx)')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, default=None, verbose_name='Unidad de Adscripción')),
                ('sede', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=10, default='SARTENEJAS', verbose_name='Sede')),
            ],
            options={
                'verbose_name_plural': 'Unidades',
                'verbose_name': 'Unidad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('ID_number', models.IntegerField(primary_key=True, serialize=False, default=0, verbose_name='Cédula')),
                ('USB_ID', models.CharField(null=True, max_length=8, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], unique=True)),
                ('first_name', models.CharField(max_length=50, default='', verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, default='', verbose_name='Apellido')),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 16, 21, 0, 882471), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], max_length=14, default=None, verbose_name='Tipo de Nómina')),
                ('type', models.CharField(choices=[('----', '----')], max_length=20, default=None, verbose_name='Tipo de Personal')),
                ('location', models.CharField(max_length=200, default=None, verbose_name='Ubicación de Trabajo')),
                ('email', models.EmailField(max_length=200, default=None, verbose_name='E-mail')),
                ('request_date', models.DateField(default=datetime.datetime(2015, 2, 18, 16, 21, 0, 882761), verbose_name='Fecha de la Solicitud')),
                ('status', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], max_length=20, default='PENDIENTE', verbose_name='Estado de la Solicitud')),
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
                ('ID_number', models.IntegerField(primary_key=True, serialize=False, default=0, verbose_name='Cédula')),
                ('USB_ID', models.CharField(null=True, max_length=8, validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], unique=True)),
                ('birthday', models.DateField(default=datetime.datetime(2015, 2, 18, 16, 21, 0, 875342), verbose_name='Fecha de Nacimiento')),
                ('paysheet', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], max_length=14, default=None, verbose_name='Tipo de Nómina')),
                ('type', models.CharField(choices=[('----', '----')], max_length=20, default=None, verbose_name='Tipo de Personal')),
                ('location', models.CharField(max_length=200, default=None, verbose_name='Ubicación de Trabajo')),
                ('finished_hours', models.IntegerField(default=0, verbose_name='Horas finalizadas')),
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
            name='ID_number',
            field=models.ForeignKey(verbose_name='Cédula', to='appProcafe.UserProfile', related_name='ID_number_remove_reques', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='USB_ID',
            field=models.ForeignKey(to_field='USB_ID', related_name='USB_ID_remove_reques', to='appProcafe.UserProfile', validators=[django.core.validators.RegexValidator(message='El USB-ID debe ser de la forma xx-xxxxx.', code='invalid_usbid', regex='^[0-9]{2}-[0-9]{5}$')], default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='removerequest',
            name='course_ID',
            field=models.ForeignKey(verbose_name='Curso', to='appProcafe.Course', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(verbose_name='Unidad', to='appProcafe.Unit', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Dpto', to='appProcafe.Department', default=None),
            preserve_default=True,
        ),
    ]
