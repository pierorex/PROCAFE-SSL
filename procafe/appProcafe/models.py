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
    ID_number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200, choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")])
    job_title = models.CharField(max_length=200)
    finished_hours = models.IntegerField(default=0)
    status = models.CharField(max_length=200)
    is_enabled = models.BooleanField(default=1)
    
    def __str__(self):  
        return "%s's profile" % self.user  



class Course(models.Model):
    department_ID = models.ForeignKey(Department, editable = False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200, choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")])
    number_hours = models.IntegerField()
    
    def __str__(self):
        return str(self.id)



class Takes(models.Model):
    user_ID = models.ForeignKey(UserProfile)
    course_ID = models.ForeignKey(Course)
    term = models.CharField(max_length=200, choices=[("SEP-DIC", "Septiembre-Diciembre"), ("ENE-MAR", "Enero-Marzo"), ("ABR-JUL", "Abril-Julio")])
    year = models.IntegerField()
    status = models.CharField(max_length=200, choices=[("APROBADO", "Aprobado"), ("REPROBADO", "Reprobado"), ("INSCRITO", "Inscrito"), ("RETIRADO", "Retirado")])


    
class Risks(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Riesgo")
    
    
    
    
    
    
    