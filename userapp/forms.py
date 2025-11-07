from django.forms import ModelForm
from userapp.models import Applied_form
from userapp.models import UserLogin


from django import forms
from .models import Applied_form

class Studentjobs(forms.ModelForm):
    class Meta:
        model = Applied_form
        fields = [
            "full_name",
            "phone_number",
            "gender",
            "date_of_birth",
            "profile_picture",
            "highest_education",
            "skills",
            "experience_years",
            "current_position",
            "preferred_job_location",
            "resume_upload",
            "linkedin_profile",
            "portfolio_link",
            "project_link",
        ]  


class EditProfile(ModelForm):
    class Meta:
        model=UserLogin
        fields=["gender","phone","address","resume","image"]


