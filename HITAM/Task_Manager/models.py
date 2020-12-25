from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Branch(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Branches"

class Key_Area(models.Model):
    name = models.CharField(max_length=300, unique=True)

class Metric(models.Model):
    key_area = models.ForeignKey(Key_Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=300,unique=True)

class AbstractUser(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        abstract = True
class FacultyUser(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
class ManagementUser(AbstractUser):
    pass
    
        
class Activity(models.Model):
    author = models.ForeignKey(FacultyUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    key_area = models.ForeignKey(Key_Area, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    freezed = models.BooleanField(default=False)
    yearandmonth = models.DateField()

    class Meta:
        verbose_name_plural = "Activities"