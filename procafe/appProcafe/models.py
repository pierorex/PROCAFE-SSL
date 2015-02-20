# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete, post_save
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail

USBIDValidator = RegexValidator(
                    regex="^[0-9]{2}-[0-9]{5}$", 
                    message="El USB-ID debe ser de la forma xx-xxxxx.", 
                    code="invalid_usbid"
                )


# Signal handlers
@receiver (pre_delete, sender=User)
def userProfile_predelete_handler(sender, instance, **kwargs):
    if instance.is_superuser:
        admins_list = []
        for user in User.objects.all():
            if user.is_superuser: admins_list.append(user)
        if len(admins_list) == 1:
            raise PermissionDenied



# Models
class Unit(models.Model):
    name = models.CharField(max_length=200, verbose_name="Unidad de Adscripción", default=None, unique=True)
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"



class Department(models.Model):
    unit_ID = models.ForeignKey(Unit, verbose_name="Unidad", default=None)
    name = models.CharField(max_length=200, verbose_name="Nombre", unique=True)
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"



class Section(models.Model):
    department_ID = models.ForeignKey(Department, verbose_name="Dpto", default=True)
    name = models.CharField(max_length=200, verbose_name="Nombre", unique=True)
    sede = models.CharField(max_length=10, verbose_name="Sede", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")], default="SARTENEJAS")

    def __str__(self):
        return str(self.department_ID) + ":" + str(self.name)

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"



class Risk(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Riesgo", unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Riesgo"
        verbose_name_plural = "Riesgos"



class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name="Cargo", unique=True)
    risks = models.ManyToManyField(Risk)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"



class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ubicación', unique=True)
    risks = models.ManyToManyField(Risk)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"


class Paysheet(models.Model):
    name = models.CharField(max_length=20, verbose_name='Tipo de Nómina', unique=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Tipo de Nómina"
        verbose_name_plural = "Tipos de Nómina"



class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Tipo de Personal', unique=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Tipo de Personal"
        verbose_name_plural = "Tipos de Personal"



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ID_number = models.IntegerField(primary_key=True, verbose_name="Cédula", default=0)
    USB_ID = models.CharField(max_length=8, unique=True, validators=[USBIDValidator], null=True)
    sex = models.CharField(max_length=10, 
                           verbose_name="Sexo", 
                           choices=[
                                    ('MASCULINO','Masculino'),
                                    ('FEMENINO','Femenino')])
    birthdate = models.DateField(verbose_name="Fecha de Nacimiento", default=datetime.today())
    paysheet = models.ForeignKey(Paysheet, verbose_name='Tipo de Nómina', default=None)
    type = models.ForeignKey(Type, verbose_name='Tipo de Personal', default=None)
    location = models.ForeignKey(Location, verbose_name='Ubicación', default=None)
    position = models.ForeignKey(Position, verbose_name="Cargo", default=None)    
    finished_hours = models.PositiveIntegerField(default=0, verbose_name="Horas finalizadas")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



class Telephone(models.Model):
    user_ID = models.ForeignKey(UserProfile, to_field='ID_number', verbose_name="Username del Trabajador", default=0)
    number = models.CharField(max_length=12, verbose_name="Número (xxxx-xxxxxxx)", validators=[RegexValidator(regex="^[0-9]{4}-[0-9]{7}$", message="El número telefónico debe ser de la forma xxxx-xxxxxxx.", code="invalid_phone")], default=None)
    
    def __str__(self):
        return str(self.number)

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
    first_name = models.CharField(max_length=50, verbose_name="Nombre", default="")
    last_name = models.CharField(max_length=50, verbose_name="Apellido", default="")
    sex = models.CharField(max_length=10, verbose_name="Sexo", default="")
    birthdate = models.DateField(verbose_name="Fecha de Nacimiento", default=datetime.today())
    paysheet = models.ForeignKey(Paysheet, verbose_name='Tipo de Nómina', default=None)
    type = models.ForeignKey(Type, verbose_name='Tipo de Personal', default=None)
    location = models.ForeignKey(Location, verbose_name='Ubicación', default=None)
    position = models.ForeignKey(Position, verbose_name="Cargo", default=None)
    email = models.EmailField(max_length=200, verbose_name="E-mail", default=None)
    request_date = models.DateField(verbose_name="Fecha de la Solicitud", default=datetime.today())
    status = models.CharField(max_length=20, 
                              verbose_name="Estado de la Solicitud", 
                              choices = [('PENDIENTE','Pendiente'),
                                         ('APROBADA','Aprobada'),
                                         ('RECHAZADA','Rechazada')], 
                              default='PENDIENTE')

    def __str__(self):
        return str(self.ID_number) + " " + str(self.request_date)
    
    class Meta:
        verbose_name = "Solicitud de Registro"
        verbose_name_plural = "Solicitudes de Registro"
        
        

# Signal handler to process UserApplications in case they get updated
@receiver (post_save, sender=UserApplication)
def userApplication_postsave_handler(sender, instance, **kwargs):
    if instance.status == 'APROBADA':
        new_user = User.objects.create_user(
                                            username = instance.first_name,
                                            email = instance.email,
                                            password = 'testing',
                                            first_name = instance.first_name,
                                            last_name = instance.last_name
                                        )
        new_user.save()

        new_userProfile = UserProfile(
                                      user = new_user,
                                      ID_number = instance.ID_number,
                                      USB_ID = instance.USB_ID,
                                      birthdate = instance.birthdate,
                                      paysheet = instance.paysheet,
                                      type = instance.type,
                                      location = instance.location,
                                      position = instance.position,
                                      sex = instance.sex
                                    )
        new_userProfile.save()
        mensaje = 'Nombre de Usuario: %d Contraseña: %s' % (new_userProfile.ID_number, 'testing')
        send_mail('Cuenta PROCAFE', 
                  mensaje, 
                  'appProcafe@procafe.usb.ve', 
                  [ '$s@mailinator.com'%(new_userProfile.ID_number),
                    new_user.email],
                  fail_silently=False)
    
    # Delete application in 2 cases: aprovada/rechazada
    if instance.status != 'PENDIENTE': instance.delete()
        
        
        
class RemoveRequest(models.Model):
    ID_number = models.ForeignKey(UserProfile, to_field='ID_number', verbose_name="Cédula", default=0, related_name='ID_number_remove_reques')
    USB_ID = models.ForeignKey(UserProfile, to_field='USB_ID', validators=[USBIDValidator], default=None, related_name='USB_ID_remove_reques')
    firstname = models.CharField(max_length=50, verbose_name="Nombre", default="")
    lastname = models.CharField(max_length=50, verbose_name="Apellido", default="")
    email = models.EmailField(max_length=200, verbose_name="E-mail", default=None)
    course_ID = models.ForeignKey(Course, verbose_name="Curso", default=None)
    request_type = models.CharField(max_length=12, verbose_name="Tipo de Solicitud", choices=[("INSCRIPCION", "Inscripción"), ("RETIRO", "Retiro")], default=None)
    request_date = models.DateField(verbose_name="Fecha de la Solicitud", default=datetime.today())
    is_pending = models.BooleanField(default=1, verbose_name="Aprobación Pendiente")
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    class Meta:
        verbose_name = "Solicitud de Cursos"
        verbose_name_plural = "Solicitudes de Cursos"


