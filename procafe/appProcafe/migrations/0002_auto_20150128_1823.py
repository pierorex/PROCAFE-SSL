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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Cursos', 'verbose_name': 'Curso'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': 'Departamentos', 'verbose_name': 'Departamento'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name_plural': 'Cargos', 'verbose_name': 'Cargo'},
        ),
        migrations.AlterModelOptions(
            name='risk',
            options={'verbose_name_plural': 'Riesgos', 'verbose_name': 'Riesgo'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': 'Secciones', 'verbose_name': 'Sección'},
        ),
        migrations.AlterModelOptions(
            name='takes',
            options={'verbose_name_plural': 'Cursa', 'verbose_name': 'Cursa'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': 'Unidades', 'verbose_name': 'Unidad'},
        ),
        migrations.AlterField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Departamento', to='appProcafe.Department'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='unit_ID',
            field=models.ForeignKey(verbose_name='Unidad superior', default=0, to='appProcafe.Unit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='department_ID',
            field=models.ForeignKey(verbose_name='Departamento', to='appProcafe.Department'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='course_ID',
            field=models.ForeignKey(verbose_name='Curso', to='appProcafe.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='status',
            field=models.CharField(choices=[('APROBADO', 'Aprobado'), ('REPROBADO', 'Reprobado'), ('INSCRITO', 'Inscrito'), ('RETIRADO', 'Retirado')], verbose_name='Estado', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='term',
            field=models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], verbose_name='Trimestre', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(verbose_name='Nombre', to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
    ]
