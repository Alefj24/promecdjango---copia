from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from .models import Cliente, Usuario, Historial, Citas, Venta, Servicio, Factura
from .forms import UsuarioForm, ClienteForm, CitaForm, FacturaForm, ServicioForm, VentaForm, HistorialForm, RegistroForm, LoginForm




# Create your views here.


def index(request):
    return render(request, 'index.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def historial(request):
    historial = Historial.objects.all()
    return render(request, 'historial.html', {'historial': historial})




def citas(request):
    citas = Citas.objects.all()
    return render(request, 'citas.html', {'citas': citas})



def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturas.html', {'facturas': facturas})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')  
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')  
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

    
@login_required
def agregar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False) 
            cita.IDCliente_id = request.user.id 
            cita.save()
            return redirect('citas')
    else:
        form = CitaForm(initial={'user_id': request.user.id})
    return render(request, 'agregar_cita.html', {'form': form})



def agregar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturas')  
    else:
        form = FacturaForm()
    return render(request, 'agregar_factura.html', {'form': form})

def agregar_servicio(request): 
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')  
    else:
        form = ServicioForm()
    return render(request, 'agregar_servicio.html', {'form': form})

def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas')  
    else:
        form = VentaForm()
    return render(request, 'agregar_venta.html', {'form': form})

def agregar_historial(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historial')  
    else:
        form = HistorialForm()
    return render(request, 'agregar_historial.html', {'form': form})


def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'form': form})



def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=cliente_id)
        cliente.delete()
        return redirect('clientes')
    else:
        return HttpResponseNotAllowed(['POST'])
    

def eliminar_venta(request, venta_id):
    if request.method == 'POST':
        venta = Venta.objects.get(pk=venta_id)
        venta.delete()
        return redirect('ventas')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def eliminar_servicio(request, servicio_id):
    if request.method == 'POST':
        servicio = Servicio.objects.get(pk=servicio_id)
        servicio.delete()
        return redirect('servicios')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def eliminar_factura(request, factura_id):
    if request.method == 'POST':
        factura = Factura.objects.get(pk=factura_id)
        factura.delete()
        return redirect('facturas')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def eliminar_cita(request, cita_id):
    if request.method == 'POST':
        cita = Citas.objects.get(pk=cita_id)
        cita.delete()
        return redirect('citas')
    else:
        return HttpResponseNotAllowed(['POST'])

def eliminar_historial(request, historial_id):
    if request.method == 'POST':
        historial = Historial.objects.get(pk=historial_id)
        historial.delete()
        return redirect('historial')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def editar_cita(request, cita_id):
    cita = get_object_or_404(Citas, pk=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'editar_cita.html', {'form': form})

def editar_factura(request, factura_id):
    factura = get_object_or_404(Factura, pk=factura_id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'editar_factura.html', {'form': form})

def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'editar_servicio.html', {'form': form})

def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'editar_venta.html', {'form': form})

def editar_historial(request, historial_id):
    historial = get_object_or_404(Historial, pk=historial_id)
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('historial')
    else:
        form = HistorialForm(instance=historial)
    return render(request, 'editar_historial.html', {'form': form})



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.Nombre_Usuario = form.cleaned_data["Nombre_Usuario"]  # Asignar el nombre de usuario
            user.email = form.cleaned_data["correo_electronico"]
            user.set_password(form.cleaned_data["password1"])
            user.save()
            Cliente = Cliente.objects.create(
                Nombre=form.cleaned_data['nombre'],
                Apellidos=form.cleaned_data['apellidos'],
                Direccion=form.cleaned_data['direccion'],
                Telefono=form.cleaned_data['telefono'],
                Correo_Electronico=form.cleaned_data['correo_electronico'],
                IDUsuario=user
            )
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


"""def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario}')
            return redirect('index') 
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})"""




"""def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})"""
    
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('index')
    
    
    
    
    

