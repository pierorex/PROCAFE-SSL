# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Cargo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Risks',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Riesgo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre de la Sección')),
                ('department_ID', models.ForeignKey(to='appProcafe.Department', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Unidad de Adscripción')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job_title',
        ),
        migrations.AddField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(to='appProcafe.Unit', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ID_number',
            field=models.IntegerField(default=0, verbose_name='Cédula', serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.ForeignKey(to='appProcafe.Position', verbose_name='Cargo', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(to='appProcafe.Department', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(verbose_name='Fecha de Fin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='init_date',
            field=models.DateTimeField(verbose_name='Fecha de Inicio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=200, verbose_name='Lugar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='number_hours',
            field=models.IntegerField(verbose_name='Número de Horas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(max_length=200, verbose_name='Tipo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre del Depto.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='course_ID',
            field=models.ForeignKey(to='appProcafe.Course', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='status',
            field=models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(to='appProcafe.UserProfile', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='year',
            field=models.IntegerField(max_length=4, verbose_name='Año'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='finished_hours',
            field=models.IntegerField(verbose_name='Horas finalizadas', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_enabled',
            field=models.BooleanField(verbose_name='Habilitado', default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(max_length=200, verbose_name='Estado'),
            preserve_default=True,
        ),
    ]
