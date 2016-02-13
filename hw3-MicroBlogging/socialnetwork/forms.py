from django import forms

from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length = 30,label='First Name',\
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 20,label='Last Name',\
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(max_length = 20,\
        widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'User Name'}))
    password1 = forms.CharField(max_length = 20,label='Password', \
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Password','type':'password'}))
    password2 = forms.CharField(label='Confirm password',\
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Confirm password', 'type':'password'}))


    #Custom validation for password1 and password2
    def clean(self):
        # Calls parent's clean function to gets a dictionary of cleaned data 
        cleaned_data = super(RegistrationForm, self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Check if two passwords don't match and raise an error
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        return cleaned_data


    #Custom validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
         
        # Check if username is present in the database and raise error if present.
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        return username

