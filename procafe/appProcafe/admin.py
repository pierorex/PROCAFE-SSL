# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appProcafe.models import Department, Unit, Section, Risk, Position, Location,\
    Paysheet, Type, CourseRequest, CourseChangeRequest
from appProcafe.models import Telephone, Document, Takes, Course
from appProcafe.models import User, UserProfile, UserApplication, RemoveRequest
from django.utils.translation import ugettext_lazy as _


admin.site.register(Department)
admin.site.register(Unit)
admin.site.register(Section)
admin.site.register(Type)
admin.site.register(Risk)
admin.site.register(Paysheet)
admin.site.register(Position)
admin.site.register(Location)

class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'number')
    
admin.site.register(Telephone, TelephoneAdmin)

class TakesAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'course_ID', 'term', 'year', 'status')

admin.site.register(Takes, TakesAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_hours')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfil'


class MyUserAdmin(UserAdmin):
    staff_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        # No permissions
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Grupos'), {'fields': ('groups',)}),
    )
    inlines = (UserProfileInLine,)
    list_display = ('username', 'email', 'get_hours')

    def get_hours(self, obj):
        return UserProfile.objects.get(user_id=obj.id).finished_hours
    get_hours.short_description = "Horas completadas"
    
    def change_view(self, request, *args, **kwargs):
        # for non-superuser
        if not request.user.is_superuser:
            try:
                self.fieldsets = self.staff_fieldsets
                response = UserAdmin.change_view(self, request, *args, **kwargs)
            finally:
                # Reset fieldsets to its original value
                self.fieldsets = UserAdmin.fieldsets
            return response
        else:
            return UserAdmin.change_view(self, request, *args, **kwargs)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

class UserApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos del Solicitante', {'fields': ('ID_number', 'USB_ID', 'first_name', 'last_name', 'birthdate', 'paysheet', 'type', 'sex', 'location', 'position', 'email')}),
        ('Solicitud', {'fields': ('request_date', 'status')}),
    )

admin.site.register(UserApplication, UserApplicationAdmin)

class RemoveRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos del Solicitante', {'fields': ('ID_number', 'USB_ID', 'first_name', 'last_name', 'email')}),
        ('Solicitud', {'fields': ('course_ID', 'request_type', 'request_date', 'status')}),
    )

admin.site.register(RemoveRequest, RemoveRequestAdmin)
