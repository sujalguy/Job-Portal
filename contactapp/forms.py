from django import forms

class complaint(forms.Form):
    Name = forms.CharField(max_length=100,label="Your Name")
    Emails = forms.EmailField(label="Your Email")
    Complaint = forms.CharField(widget=forms.Textarea,label="Write a application ")