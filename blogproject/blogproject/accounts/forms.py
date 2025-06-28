from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=30, required=False, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'website', 'birthdate']
        labels = {
            'avatar': 'Foto de perfil',
            'bio': 'Biografía',
            'website': 'Sitio web',
            'birthdate': 'Fecha de nacimiento',
        }