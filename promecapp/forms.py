from django import forms
from .models import Usuario, Cliente, Servicio, Factura, Venta, Historial, Citas
from django.contrib.auth.models import User

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
    class Meta:
        model = Citas
        fields = ['Fecha_Hora', 'Descripcion', 'IDEstado', 'IDCliente']
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
        


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['Nombre_Usuario', 'password1', 'password2']  # Campos de Usuario y Contraseña

    # Agregar campos de Cliente como campos adicionales en el formulario
    nombre = forms.CharField(label='Nombre', max_length=45)
    apellidos = forms.CharField(label='Apellidos', max_length=45)
    direccion = forms.CharField(label='Direccion', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=10)
    correo_electronico = forms.EmailField(label='Correo Electrónico')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
            # Crear un nuevo cliente asociado al usuario
            Cliente.objects.create(
                Nombre=self.cleaned_data['nombre'],
                Apellidos=self.cleaned_data['apellidos'],
                Direccion=self.cleaned_data['direccion'],
                Telefono=self.cleaned_data['telefono'],
                Correo_Electronico=self.cleaned_data['correo_electronico'],
                IDUsuario=usuario
            )
        return usuario
