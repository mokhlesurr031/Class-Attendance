from django.contrib import admin

# Register your models here.

from .models import StudentAttendance, AttendanceManager


admin.site.register(StudentAttendance)
