from django import forms
from .models import Users

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs=
                    {'class': 'form-control'}),
            'password': forms.PasswordInput(attrs=
                    {'class': 'form-control'}),
            
        }
