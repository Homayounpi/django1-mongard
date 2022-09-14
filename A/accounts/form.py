from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password=forms.CharField()
    last_name=forms.CharField()
    first_name=forms.CharField()

class UserloginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

