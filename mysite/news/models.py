from django.db import models

# Create your models here.
from django.db import models

class Report(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    Report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Homework(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
