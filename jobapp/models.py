from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Itjobs(models.Model):
    Company_name=models.CharField(max_length=100)
    Job_title=models.CharField(max_length=100)
    Job_location=models.CharField(max_length=100)
    Experience=models.FloatField()
    Salary=models.FloatField()
    Job_description=models.TextField(blank=True, null= True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True,default=None)  # Recruiter who posted
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Company_name



class MECHjobs(models.Model):
    Company_name=models.CharField(max_length=100)
    Job_title=models.CharField(max_length=100)
    Job_location=models.CharField(max_length=100)
    Experience=models.FloatField()
    Salary=models.FloatField()
    Job_description=models.TextField(blank=True, null= True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True,default=None)  # Recruiter who posted
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Company_name
    



class CIVILjobs(models.Model):
    Company_name=models.CharField(max_length=100)
    Job_title=models.CharField(max_length=100)
    Job_location=models.CharField(max_length=100)
    Experience=models.FloatField()
    Salary=models.FloatField()
    Job_description=models.TextField(blank=True, null= True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True,default=None)  # Recruiter who posted
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.Company_name





class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('user', 'User'),
    ]
    email=models.EmailField("Email",unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    def __str__(self):
        return f"{self.username} ({self.role})"
