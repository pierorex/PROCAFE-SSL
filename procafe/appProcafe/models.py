from django.db import models
from django.contrib.auth.models import User
from django import utils


class Department(models.Model):
    departament_ID = models.IntegerField(primary_key = True)
    name = models.CharField()



class UserProfile(models.Model):  
    user = models.ForeignKey(User)
    ID_number = models.IntegerField(primary_key=True)
    type = models.CharField(choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")])
    job_title = models.CharField()
    finished_hours = models.IntegerField(default=0)
    status = models.CharField()
    is_enabled = models.BooleanField(default=1)
    
    def __str__(self):  
        return "%s's profile" % self.user  

    def create_user_profile(self):  #REVISARRRR
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)  



class Course(models.Model):
    course_ID = models.IntegerField(primary_key = True)
    department_ID = models.ForeignKey(Department)
    name = models.CharField()
    type = models.CharField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")])
    number_hours = models.IntegerField()



class Takes(models.Model):
    user_ID = models.ForeignKey(UserProfile)
    course_ID = models.ForeignKey(Course)
    term = models.CharField(choices=[("SEP-DIC", "Septiembre-Diciembre"), ("ENE-MAR", "Enero-Marzo"), ("ABR-JUL", "Abril-Julio")])
    year = models.IntegerField()
    status = models.CharField(choices=[("Aprobado", "APROBADO"), ("Reprobado", "REPROBADO"), ("Inscrito", "INSCRITO"), ("Retirado", "RETIRADO")])
    







class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self): return self.pub_date >= utils.timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = pub_date
    was_published_recently.boolean = True
    was_published_recently.short_desc = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    