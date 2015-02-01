# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appProcafe.models import *


admin.site.register(Department)
admin.site.register(Unit)
admin.site.register(Section)
admin.site.register(Risk)
admin.site.register(Position)
admin.site.register(Telephone)
admin.site.register(Document)

class TakesAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'course_ID', 'term', 'year', 'status')

admin.site.register(Takes, TakesAdmin)

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {'fields': ['name', 'department_ID', 'modality', 'number_hours', 'location']}),
        ('Descripción', {'fields': ['description', 'video_url']}),
        ('Fechas', {'fields': ['init_date', 'end_date']}),
    ]

    list_display = ('name', 'department_ID', 'number_hours')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInLine,)
    list_display = ('username', 'email', 'get_hours')

    def get_hours(self, obj):
        return UserProfile.objects.get(user_id=obj.id).finished_hours
    get_hours.short_description = "Horas completadas"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

