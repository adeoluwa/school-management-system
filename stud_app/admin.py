from django.contrib import admin

from stud_app.models import *

admin.site.site_header = 'School managment System'

# Register your models here.
admin.site.register(Student)

admin.site.register(Staff)