from django import forms
from .models import Usuario, Cliente, Servicio, Factura, Venta, Historial, Citas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre_Usuario', 'Contraseña', 'IDRol']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nombre', 'Apellidos', 'Direccion', 'Telefono', 'Correo_Electronico', 'IDUsuario']
        

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['Nombre_Servicio', 'Descripcion', ]
        
class  FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['Fecha', 'Total','Descripcion','IDVenta']
        
class  VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Fecha_Venta', 'Monto_Total','descripcion','IDServicio','IDTipo_pago','IDCita']
        widgets = {
            'Fecha_Venta': forms.DateInput(attrs={'type': 'date'})}
        
class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['Descripcion', 'valor','Fecha','IDCliente']
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'})}
        
class CitaForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput())  # Campo oculto para el ID del usuario

    class Meta:
        model = Citas
        fields = ['Fecha_Hora', 'Descripcion', 'IDEstado', 'user_id']
        widgets = {
            'Fecha_Hora': forms.DateTimeInput(attrs={'type': 'datetime-local'})}


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['Fecha', 'Total', 'Descripcion', 'IDVenta']
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'})}
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['Nombre_Servicio', 'Descripcion']
        


class RegistroForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre', max_length=45)
    apellidos = forms.CharField(label='Apellidos', max_length=45)
    direccion = forms.CharField(label='Direccion', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=10)
    correo_electronico = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['correo_electronico']
        if commit:
            user.save()
            Cliente.objects.create(
                Nombre=self.cleaned_data['nombre'],
                Apellidos=self.cleaned_data['apellidos'],
                Direccion=self.cleaned_data['direccion'],
                Telefono=self.cleaned_data['telefono'],
                Correo_Electronico=self.cleaned_data['correo_electronico'],
                IDUsuario=user
            )
        return user
    
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
