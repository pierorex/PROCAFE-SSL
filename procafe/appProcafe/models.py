from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Unidad de Adscripción")



class Department(models.Model):
    unit_ID = models.ForeignKey(Unit)
    name = models.CharField(max_length=200, verbose_name = "Nombre del Depto.")
    
    def __str__(self):
        return str(self.id)
    
    

class Section(models.Model):
    department_ID = models.ForeignKey(Department, editable = False)
    name = models.CharField(max_length=200, verbose_name = "Nombre de la Sección")



class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Cargo")



class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    ID_number = models.IntegerField(primary_key=True, verbose_name = "Cédula")
    type = models.CharField(max_length=200, choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")])
    position = models.ForeignKey(Position, verbose_name = "Cargo")
    finished_hours = models.IntegerField(default=0, verbose_name = "Horas finalizadas")
    status = models.CharField(max_length=200, verbose_name = "Estado")
    is_enabled = models.BooleanField(default=1, verbose_name = "Habilitado")
    
    def __str__(self):  
        return "%s's profile" % self.user  



class Course(models.Model):
    department_ID = models.ForeignKey(Department, editable = False)
    name = models.CharField(max_length=200, verbose_name = "Nombre")
    type = models.CharField(max_length=200, verbose_name = "Tipo")
    init_date = models.DateTimeField(verbose_name = "Fecha de Inicio")
    end_date = models.DateTimeField(verbose_name = "Fecha de Fin")
    location = models.CharField(max_length=200, verbose_name = "Lugar", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")])
    number_hours = models.IntegerField(verbose_name = "Número de Horas")
    
    def __str__(self):
        return str(self.id)



class Takes(models.Model):
    user_ID = models.ForeignKey(UserProfile, editable = False)
    course_ID = models.ForeignKey(Course, editable = False)
    term = models.CharField(max_length=200, choices=[("SEP-DIC", "Septiembre-Diciembre"), ("ENE-MAR", "Enero-Marzo"), ("ABR-JUL", "Abril-Julio")])
    year = models.IntegerField(max_length=4, verbose_name = "Año")
    status = models.CharField(max_length=200, choices=[("APROBADO", "Aprobado"), ("REPROBADO", "Reprobado"), ("INSCRITO", "Inscrito"), ("RETIRADO", "Retirado")])


    
class Risks(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Riesgo")
    
    
    
    
    
    
    