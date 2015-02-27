# -*- coding: utf-8 -*-
# Functions used all over appProcafe
from appProcafe.models import UserProfile, User
import re
import datetime

#no se admite que en el archivo exel alguna casilla tenga escrito un " doble comilla, de ser asi el comportamiento de esta funcion puede ser inesperado
#solo se toman los primeros 3 campos porque los demas se suponen que estan incorrectos
linestipo = re.compile(r"^([0-9]+),(([^\",]+)|(\"[^\"]+\")),(([^\",]+)|(\"[^\"]+\")),(([^\",]+)|(\"[^\"]+\")),(([^\",]+)|(\"[^\"]+\")),(([^\",]+)|(\"[^\"]+\")),(([^\",]+)|(\"[^\"]+\")),*$")#si, esto es una expresion regular

def csv_to_UserProfile(file_path):
    with open(file_path, "r") as myfile:
        data = myfile.read()

    for line2 in data.split("\n")[1:]:
        match = linestipo.match(line2)
        if match:
            cedula = match.group(1)
            l = len(match.group(2))-1
            if(match.group(2)[0] == '"' and match.group(2)[l] == '"'):
                nombre = match.group(2)[1:l]
            else:
                nombre = match.group(2)
            l = len(match.group(5))-1
            if(match.group(5)[0] == '"' and match.group(5)[l] == '"'):
                apellido = match.group(5)[1:l]
            else:
                apellido = match.group(5)

            try: #consultando BD para ver si existe usuario con esta cedula
                consulta = UserProfile.objects.get(ID_number = int(cedula))
            except UserProfile.DoesNotExist:
                consulta = None

            if (consulta==None): #crea user y userprofile si no existe
                usernametemp = (nombre + apellido).split(" ")
                name = ''
                for n in usernametemp:
                    name+=n
                if (User.objects.filter(username = name).exists()):
                    name+=cedula
                new_user = User.objects.create_user(
                                            username = name,
                                            email = 'ProcafeTest@mailinator.com',
                                            password = 'testing',
                                            first_name = nombre,
                                            last_name = apellido
                                        )
                new_user.is_active = True
                new_user.save()
                new_userProfile = UserProfile(
                                      user = new_user,
                                      ID_number = int(cedula),
                                      USB_ID = None,
                                      birthdate = None,
                                      paysheet = None,
                                      type = None,
                                      location = None,
                                      position = None,
                                      sex = None,
                                      finished_hours = 0
                                    )
                new_userProfile.save()
            else:
                user = consulta.user
                user.is_active = True
                user.save()
        else:
            continue