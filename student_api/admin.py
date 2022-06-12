from django.contrib import admin

from student_api.models import Path, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Path)
