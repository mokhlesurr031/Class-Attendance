from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import SearchEnrolledStudentForm
from student.models import EnrolledStudent
from academic.models import ClassRegistration
from .models import StudentAttendance
import json

def student_attendance(request):
    forms = SearchEnrolledStudentForm()
    class_name = request.GET.get('reg_class', None)
    if class_name:
        class_info = ClassRegistration.objects.get(id=class_name)
        student = EnrolledStudent.objects.filter(class_name=class_name)
        context = {
            'forms': forms,
            'student': student,
            'class_info': class_info
        }
        return render(request, 'attendance/student-attendance.html', context)
    context = {
        'forms': forms,
    }
    return render(request, 'attendance/student-attendance.html', context)

class SetAttendance(APIView):
    def get(self, request, std_class, std_roll):
        try:
            StudentAttendance.objects.create_attendance(std_class, std_roll)
            return Response({'status': 'Success'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)



def attendance_report(request, **kwargs):
    try:
        body_unicode = request.body.decode('utf-8')
        date = body_unicode[-10:]
        attendance = StudentAttendance.objects.filter(date=date)
        context = {
            'attendance': attendance
        }
        return render(request, 'attendance/attendance-list.html', context)

    except:
        return render(request, 'attendance/attendance-list.html')

