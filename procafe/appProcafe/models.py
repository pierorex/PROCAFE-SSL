from django.db import models
from django.contrib.auth.models import User



class Department(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)



class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200, choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")])
    job_title = models.CharField(max_length=200)
    finished_hours = models.IntegerField(default=0)
    status = models.CharField(max_length=200)
    is_enabled = models.BooleanField(default=1)
    
    def __str__(self):  
        return "%s's profile" % self.user  



class Course(models.Model):
    id = models.IntegerField(primary_key = True, editable = False)
    department_ID = models.ForeignKey(Department)
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


    