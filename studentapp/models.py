from django.db import models

# Create your models here.
class Student(models.Model):
    assign_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    uploadby = models.CharField(max_length=20)

    def __str__(self):
        return self.title
