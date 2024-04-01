from django.shortcuts import render, redirect
from .models import Cliente, Usuario, Historial, Citas, Venta, Servicio, Factura
from .forms import UsuarioForm
# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

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