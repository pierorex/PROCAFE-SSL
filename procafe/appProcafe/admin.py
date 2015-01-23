from django.contrib import admin
from appProcafe.models import *



admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Unit)
admin.site.register(Section)
admin.site.register(Risk)
admin.site.register(Position)
admin.site.register(Takes)

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {'fields': ['name', 'department_ID', 'type', 'number_hours', 'location']}),
        ('Fechas', {'fields': ['init_date', 'end_date']}),
    ]

    list_display = ('name', 'department_ID', 'number_hours')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
