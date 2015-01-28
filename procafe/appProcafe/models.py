from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Unidad de Adscripción")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"



class Department(models.Model):
    unit_ID = models.ForeignKey(Unit, verbose_name = "Unidad superior", default = 0)
    name = models.CharField(max_length=200, verbose_name = "Nombre")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"



class Section(models.Model):
    department_ID = models.ForeignKey(Department, verbose_name = "Departamento", editable = True)
    name = models.CharField(max_length=200, verbose_name = "Nombre")

    def __str__(self):
        return str(self.department_ID) + ":" + str(self.name)

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"


class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Cargo")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ID_number = models.IntegerField(primary_key=True, default = 0, verbose_name = "Cédula")
    type = models.CharField(max_length=200, choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")])
    position = models.ForeignKey(Position, default = 0, verbose_name = "Cargo")
    finished_hours = models.IntegerField(default=0, verbose_name = "Horas finalizadas")
    status = models.CharField(max_length=200, verbose_name = "Estado")
    is_enabled = models.BooleanField(default=1, verbose_name = "Habilitado")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



class Course(models.Model):
    department_ID = models.ForeignKey(Department, verbose_name = "Departamento")
    name = models.CharField(max_length=200, verbose_name = "Nombre")
    description = models.CharField(max_length=200, verbose_name = "Descripcion", default = None)
    video_url = models.CharField(max_length=1000, verbose_name = "URL del video")
    type = models.CharField(max_length=200, verbose_name = "Tipo", choices=[("PRESENCIAL","Presencial"),("A DISTANCIA", "A distancia")])
    init_date = models.DateTimeField(verbose_name = "Fecha de Inicio")
    end_date = models.DateTimeField(verbose_name = "Fecha de Fin")
    location = models.CharField(max_length=200, verbose_name = "Lugar", choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")])
    number_hours = models.IntegerField(verbose_name = "Número de Horas")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"



class Takes(models.Model):
    user_ID = models.ForeignKey(UserProfile, editable = True, verbose_name="Nombre")
    course_ID = models.ForeignKey(Course, editable = True, verbose_name="Curso")
    term = models.CharField(max_length=200, verbose_name = "Trimestre", choices=[("SEP-DIC", "Septiembre-Diciembre"), ("ENE-MAR", "Enero-Marzo"), ("ABR-JUL", "Abril-Julio")])
    year = models.IntegerField(max_length=4, verbose_name = "Año")
    status = models.CharField(max_length=200, verbose_name = "Estado", choices=[("APROBADO", "Aprobado"), ("REPROBADO", "Reprobado"), ("INSCRITO", "Inscrito"), ("RETIRADO", "Retirado")])

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
    file = models.FileField (upload_to='documents/%Y/%m/%d')

