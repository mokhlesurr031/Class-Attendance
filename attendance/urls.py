from django.urls import path
from .views import student_attendance, SetAttendance, attendance_report

urlpatterns = [
    path('student/', student_attendance, name='student-attendance'),
    path('set-attendance/<std_class>/<std_roll>', SetAttendance.as_view(), name='set-attendance'),
    path('attendance_report/', attendance_report, name='attendance_report'),
    # path('attendance_report/post/', attendance_report, name='attendance_report_post')
]