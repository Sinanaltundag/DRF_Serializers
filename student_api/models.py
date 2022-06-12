from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Path(models.Model):
    path_name = models.CharField(max_length=10)

    def __repr__(self):
        return self.path_name

class Student(models.Model):
    path= models.ForeignKey(Path, related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    # blank=True for admin dashboard
    # null=True for db
    def __str__(self):
        return f"{self.last_name} {self.first_name}"