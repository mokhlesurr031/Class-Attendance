from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Upazilla(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Union(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name