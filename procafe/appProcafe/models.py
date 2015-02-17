# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

USBIDValidator = RegexValidator(
                    regex="^[0-9]{2}-[0-9]{5}$", 
                    message="El USB-ID debe ser de la forma xx-xxxxx.", 
                    code="invalid_usbid"
                )


class Unit(models.Model):
    name = models.CharField(max_length=200, verbose_name="Unidad de Adscripción", default=None)
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"



class Department(models.Model):
    unit_ID = models.ForeignKey(Unit, verbose_name="Unidad", default=None)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"



class Section(models.Model):
    department_ID = models.ForeignKey(Department, verbose_name="Dpto", default=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.department_ID) + ":" + str(self.name)

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"



class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name="Cargo")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ID_number = models.IntegerField(primary_key=True, verbose_name="Cédula", default=0)
    USB_ID = models.CharField(max_length=8, unique=True, validators=[USBIDValidator], null=True)
    firstname = models.CharField(max_length=50, verbose_name="Nombre", default="")
    lastname = models.CharField(max_length=50, verbose_name="Apellido", default="")
    birthday = models.DateField(verbose_name="Fecha de Nacimiento", default=datetime.today())
    paysheet = models.CharField(max_length=14, verbose_name="Tipo de Nómina", choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")], default=None)
    type = models.CharField(max_length=20, choices=[("----", "----")], verbose_name="Tipo de Personal", default=None)
    location = models.CharField(max_length=200, verbose_name="Ubicación de Trabajo", default=None)
    position = models.ForeignKey(Position, verbose_name="Cargo", default=None)
    email = models.EmailField(verbose_name="E-mail", default=None)
    
    finished_hours = models.IntegerField(default=0, verbose_name="Horas finalizadas")
    is_enabled = models.BooleanField(default=1, verbose_name="Habilitado")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



class Telephone(models.Model):
    user_ID = models.ForeignKey(UserProfile, to_field='ID_number', verbose_name="Cédula del Trabajador", default=0)
    number = models.CharField(max_length=12, verbose_name="Número (xxxx-xxxxxxx)", validators=[RegexValidator(regex="^[0-9]{4}-[0-9]{7}$", message="El número telefónico debe ser de la forma xxxx-xxxxxxx.", code="invalid_phone")], default=None)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Teléfono"
        verbose_name_plural = "Teléfonos"



class Course(models.Model):
    department_ID = models.ForeignKey(Department, verbose_name="Dpto", default=None)
    name = models.CharField(primary_key=True, max_length=200, verbose_name="Nombre", default=None)
    description = models.CharField(max_length=200, verbose_name = "Descripción", default=None)
    content = models.CharField(max_length=200, verbose_name="Contenido", default=None)
    video_url = models.URLField(max_length=1000, verbose_name = "URL del video", default=None)
    modality = models.CharField(max_length=200, verbose_name="Modalidad", choices=[("PRESENCIAL","Presencial"),("DISTANCIA", "A distancia")], default="PRESENCIAL")
    instructor = models.CharField(max_length=200, verbose_name="Instructor", default=None)
    init_date = models.DateTimeField(verbose_name="Fecha de Inicio")
    end_date = models.DateTimeField(verbose_name="Fecha de Fin")
    location = models.CharField(max_length=200, verbose_name="Lugar", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")
    number_hours = models.IntegerField(verbose_name="Número de Horas")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"



class Takes(models.Model):
    user_ID = models.ForeignKey(UserProfile, verbose_name="Nombre", default=None)
    course_ID = models.ForeignKey(Course, verbose_name="Curso", default=None)
    term = models.CharField(max_length=200, verbose_name="Trimestre", choices=[("SEP-DIC", "Septiembre-Diciembre"), ("ENE-MAR", "Enero-Marzo"), ("ABR-JUL", "Abril-Julio")], default="SEP-DIC")
    year = models.IntegerField(max_length=4, verbose_name="Año")
    status = models.CharField(max_length=200, verbose_name="Estado", choices=[("APROBADO", "Aprobado"), ("REPROBADO", "Reprobado"), ("INSCRITO", "Inscrito"), ("RETIRADO", "Retirado")], default=None)

    class Meta:
        verbose_name = "Cursa"
        verbose_name_plural = "Cursa"



class Risk(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Riesgo")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Riesgo"
        verbose_name_plural = "Riesgos"

class Document(models.Model):
    file = models.FileField(upload_to='documents')
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        


class UserApplication(models.Model):
    ID_number = models.IntegerField(primary_key=True, verbose_name="Cédula", default=0)
    USB_ID = models.CharField(max_length=8, unique=True, validators=[USBIDValidator], null=True)
    firstname = models.CharField(max_length=50, verbose_name="Nombre", default="")
    lastname = models.CharField(max_length=50, verbose_name="Apellido", default="")
    birthday = models.DateField(verbose_name="Fecha de Nacimiento", default=datetime.today())
    paysheet = models.CharField(max_length=14, verbose_name="Tipo de Nómina", choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")], default=None)
    type = models.CharField(max_length=20, choices=[("----", "----")], verbose_name="Tipo de Personal", default=None)
    location = models.CharField(max_length=200, verbose_name="Ubicación de Trabajo", default=None)
    position = models.ForeignKey(Position, verbose_name="Cargo", default=None)
    email = models.EmailField(max_length=200, verbose_name="E-mail", default=None)
    request_date = models.DateField(verbose_name="Fecha de la Solicitud", default=datetime.today())
    is_pending = models.BooleanField(default=1, verbose_name="Aprobación Pendiente")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    class Meta:
        verbose_name = "Solicitud de Registro"
        verbose_name_plural = "Solicitudes de Registro"
        
        
        
class RemoveRequest(models.Model):
    ID_number = models.ForeignKey(UserProfile, to_field='ID_number', verbose_name="Cédula", default=0)
    USB_ID = models.ForeignKey(UserProfile, to_field='USB_ID', validators=[USBIDValidator], default=None)
    firstname = models.CharField(max_length=50, verbose_name="Nombre", default="")
    lastname = models.CharField(max_length=50, verbose_name="Apellido", default="")
    email = models.EmailField(max_length=200, verbose_name="E-mail", default=None)
    course_ID = models.ForeignKey(Course, verbose_name="Curso", default=None)
    request_type = models.CharField(verbose_name="Tipo de Solicitud", choices=[("INSCRIPCION", "Inscripción"), ("RETIRO", "Retiro")], default=None)
    request_date = models.DateField(verbose_name="Fecha de la Solicitud", default=datetime.today())
    is_pending = models.BooleanField(default=1, verbose_name="Aprobación Pendiente")
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    class Meta:
        verbose_name = "Solicitud de Cursos"
        verbose_name_plural = "Solicitudes de Cursos"
