from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre_Usuario', 'Contraseña', 'IDRol']
