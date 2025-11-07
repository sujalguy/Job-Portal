from django.forms import ModelForm
from jobapp.models import Itjobs 
from jobapp.models import MECHjobs
from jobapp.models import CIVILjobs
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CreateItJobsForm(ModelForm):
    class Meta:
        model= Itjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']




class UpdateItJobsForm(ModelForm):
    class Meta:
        model= Itjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']


class CreateMechjobsform(ModelForm):
    class Meta:
        model=MECHjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']


class UpdateMechJobs(ModelForm):
    class Meta:
        model=MECHjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']



class CreateCIVILjobsform(ModelForm):
    class Meta:
        model=CIVILjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']


class UpdateCivilJobs(ModelForm):
    class Meta:
        model=CIVILjobs
        fields=['Company_name', 'Job_title', 'Job_location', 'Experience', 'Salary', 'Job_description']



class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



    
    