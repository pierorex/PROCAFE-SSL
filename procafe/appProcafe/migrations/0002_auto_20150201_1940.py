# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProcafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelOptions(
            name='risk',
            options={'verbose_name': 'Riesgo', 'verbose_name_plural': 'Riesgos'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterModelOptions(
            name='takes',
            options={'verbose_name': 'Cursa', 'verbose_name_plural': 'Cursa'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Unidad', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AlterField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Departamento', to='appProcafe.Department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_hours',
            field=models.IntegerField(verbose_name='NAmero de Horas'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=200),
        ),
        migrations.AlterField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(verbose_name='Unidad superior', default=0, to='appProcafe.Unit'),
        ),
        migrations.AlterField(
            model_name='section',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Departamento', to='appProcafe.Department'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=200),
        ),
        migrations.AlterField(
            model_name='takes',
            name='course_ID',
            field=models.ForeignKey(verbose_name='Curso', to='appProcafe.Course'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='status',
            field=models.CharField(verbose_name='Estado', choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], max_length=200),
        ),
        migrations.AlterField(
            model_name='takes',
            name='term',
            field=models.CharField(verbose_name='Trimestre', choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], max_length=200),
        ),
        migrations.AlterField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Nombre', to='appProcafe.UserProfile'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='year',
            field=models.IntegerField(verbose_name='AAo', max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('ACADEMICO', 'AcadAmico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], max_length=200),
        ),
    ]
