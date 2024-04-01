from django import forms
from .models import Usuario, Cliente

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre_Usuario', 'Contraseña', 'IDRol']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nombre', 'Apellidos', 'Direccion', 'Telefono', 'Correo_Electronico', 'IDUsuario']