from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from datetime import datetime
from django.utils import timezone



from django.conf import settings

class UserLogin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[("Male","Male"),("Female","Female"),("Other","Other")])
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    image = models.ImageField(upload_to="profile_images/", blank=True, null=True) 


    def __str__(self):
        return self.user.username

class Applied_form(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)

    job_type = models.CharField(max_length=20,default="Unknown",null=True,blank=True)

    job_id = models.PositiveIntegerField(null=True,blank=True)

    applied_at = models.DateTimeField(default=timezone.now,null=True,blank=True)
  

    GENDER_CHOICE = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other"),
    ]
    
    mob_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Enter a valid 10-digit mobile number"
    )



    
    full_name = models.CharField("Full Name", max_length=100, blank=True, null=True)
    phone_number = models.CharField("Phone Number", max_length=15, validators=[mob_regex])
    gender = models.CharField("Gender", max_length=20, choices=GENDER_CHOICE, default="Other")
    date_of_birth = models.DateField("Birth Of Date", null=True, blank=True)
    profile_picture = models.ImageField("Profile Picture", upload_to="profile_pics/", null=True, blank=True)

    highest_education = models.CharField("Highest Education", max_length=100, blank=True, null=True)
    skills = models.TextField("Skills", blank=True, null=True)
    experience_years = models.PositiveIntegerField("Experience Years", default=0, blank=True)
    current_position = models.CharField("Current Position", max_length=100, blank=True, null=True)
    preferred_job_location = models.CharField("Preferred Job Location", max_length=100, blank=True, null=True)

    resume_upload = models.FileField("Resume Upload", upload_to="resumes/", blank=True, null=True)
    linkedin_profile = models.URLField("LinkedIn Profile", blank=True, null=True)
    portfolio_link = models.URLField("Portfolio Link", blank=True, null=True)
    project_link = models.URLField("Project Link", blank=True, null=True)

    status = models.CharField(max_length=20, choices=[
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
    ], default="Pending")


    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"
        ordering = ["full_name"]



    def __str__(self):
        return f"{self.full_name}- {self.job_type} ({self.job_id})"