from django.db import models
from django.urls import reverse


# Create your models here.
#
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})
