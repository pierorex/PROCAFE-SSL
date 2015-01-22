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
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(choices=[('SARTENEJAS', 'Sartenejas'), ('LITORAL', 'Litoral')], max_length=200)),
                ('number_hours', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('term', models.CharField(choices=[('SEP-DIC', 'Septiembre-Diciembre'), ('ENE-MAR', 'Enero-Marzo'), ('ABR-JUL', 'Abril-Julio')], max_length=200)),
                ('year', models.IntegerField()),
                ('status', models.CharField(choices=[('Aprobado', 'APROBADO'), ('Reprobado', 'REPROBADO'), ('Inscrito', 'INSCRITO'), ('Retirado', 'RETIRADO')], max_length=200)),
                ('course_ID', models.ForeignKey(to='appProcafe.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo'), ('OBRERO', 'Obrero')], max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('finished_hours', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
                ('is_enabled', models.BooleanField(default=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='takes',
            name='user_ID',
            field=models.ForeignKey(to='appProcafe.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department_ID',
            field=models.ForeignKey(to='appProcafe.Department'),
            preserve_default=True,
        ),
    ]
