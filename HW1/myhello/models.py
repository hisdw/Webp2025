from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    Department=models.CharField(max_length=150, default="Unknown")
    CourseTitle=models.CharField(max_length=150, default="Unknown")
    Instructor=models.CharField(max_length=150, default="Unknown")
    #location=models.CharField(max_length=100)
    #created_at=models.DateTimeField(auto_now_add=True)