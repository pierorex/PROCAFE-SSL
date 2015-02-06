# -*- coding: utf-8 -*-
# Functions used all over appProcafe
from appProcafe.models import UserProfile, User


def csv_to_UserProfile(file_path):
    with open(file_path, "r") as myfile:
        data = myfile.read()
    for line in data.split("\n"):
        line = line.split(",")
        if (not UserProfile.objects.filter(ID_number = int(line[0])).exists()):
            u = User.objects.create_user(line[1],'a@a.com','hola')
            u.first_name = line[1]
            u.last_name = line[2]
            u.save()
            p = UserProfile(user_id = u.id,
                            ID_number = int(line[0]),
                            type = "Academico",
                            finished_hours = 0,
                            status = "no se que va aqui",
                            is_enabled = 1)
            p.save()
        #else se puede activar el usuario