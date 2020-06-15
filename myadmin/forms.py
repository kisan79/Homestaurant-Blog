#All Forms of Admin Here
from django import forms
from .models import Admin

#Admin-Login Form
class AdminLoginForm(forms.Form):
    username=forms.CharField(
        max_length=10,
        label="USERNAME",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username or Email'})
    )
    password=forms.CharField(
        label='PASSWORD',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
    )

#Admin -Register model
class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Give an Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control-lg','placeholder':'Enter Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control-lg','placeholder':'Enter Your Email'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control-lg','placeholder':'Enter 10 Digit No'}),
            'first_name':forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Enter Last Name'}),
            'photo':forms.FileInput(attrs={'class':'form-control-file-lg'}),
        }