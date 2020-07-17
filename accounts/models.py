from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='admin/')
    gender_choice = (
        ('male', 'Male'),
        ('female', 'female')
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    employee_choice = (
        ('admin', 'Admin'),
        ('proffessor', 'Proffessor'),
        ('teacher', 'Teacher'),
        ('register', 'Professor'),
        ('student', 'Student')

    )

    employee_type = models.CharField(choices=employee_choice, max_length=20)

    def __str__(self):
        return self.name