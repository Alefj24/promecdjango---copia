from django.db import models

class Rol(models.Model):
    IDRol = models.AutoField(primary_key=True)
    Nombre_Rol = models.CharField(max_length=50, unique=True)
    Descripcion = models.TextField()

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.Nombre_Rol

class TipoPago(models.Model):
    idTipo_pago = models.AutoField(primary_key=True)
    nombre_pago = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'Tipo_pago'

    def __str__(self):
        return self.nombre_pago


class Estado(models.Model):
    idestado = models.AutoField(primary_key=True)
    Nombre_estado = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.Nombre_estado

class Usuario(models.Model):
    IDUsuario = models.AutoField(primary_key=True)
    Nombre_Usuario = models.CharField(max_length=50, unique=True)
    Contraseña = models.CharField(max_length=50)
    IDRol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.Nombre_Usuario

class Cliente(models.Model):
    IDCliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10, unique=True)
    Correo_Electronico = models.CharField(max_length=50, unique=True)
    IDUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"
    


class Historial(models.Model):
    IDHistorial = models.AutoField(primary_key=True)
    Descripcion = models.TextField()
    valor = models.IntegerField()
    Fecha = models.DateField()
    IDCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'historial'

class Citas(models.Model):
    IDCita = models.AutoField(primary_key=True)
    Fecha_Hora = models.DateTimeField()
    Descripcion = models.TextField(null=True)
    IDEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    IDCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'citas'

    def __str__(self):
        return str(self.IDCita)



class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Total = models.DecimalField(max_digits=15, decimal_places=2)
    Descripcion = models.CharField(max_length=100, null=True)
    IDVenta = models.ForeignKey('Venta', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Factura'



class Servicio(models.Model):
    IDServicio = models.AutoField(primary_key=True)
    Nombre_Servicio = models.CharField(max_length=30, unique=True)
    Descripcion = models.TextField()

    class Meta:
        db_table = 'servicios'

    def __str__(self):
        return self.Nombre_Servicio

class Venta(models.Model):
    IDVenta = models.AutoField(primary_key=True)
    Fecha_Venta = models.DateField()
    Monto_Total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    IDServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    IDTipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    IDCita = models.ForeignKey(Citas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'venta'

    def __str__(self):
        return str(self.IDVenta)

