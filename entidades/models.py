from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

#-------------------------------------------------------------------------------------------------------------------------------
#vehiculos

class CantidadPasajeros(models.Model):
    cantidad = models.CharField(max_length=50)

    def __str__(self):
        return self.cantidad

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    pasajeros = models.ForeignKey(CantidadPasajeros, on_delete=models.CASCADE, null=True, default=None)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}/ año {}".format(self.marca, self.modelo, self.año)

    class Meta:
        verbose_name = "Automóvil"
        verbose_name_plural = "Automóviles"
        ordering = ["modelo", "marca", "año"]

#-------------------------------------------------------------------------------------------------------------------------------
#camioneta

class Cabina(models.Model):
    cabina = models.CharField(max_length=50)
    def __str__(self):
        return self.cabina

class Traccion(models.Model):
    traccion = models.CharField(max_length=50)
    def __str__(self):
        return self.traccion

class Camioneta(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    traccion = models.ForeignKey(Traccion, on_delete=models.CASCADE, null=True, default=None)
    tipo_cabina = models.ForeignKey(Cabina, on_delete=models.CASCADE, null=True, default=None)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}/ año {}".format(self.marca, self.modelo, self.año)

    class Meta:
        verbose_name = "Camioneta"
        verbose_name_plural = "Camionetas"
        ordering = ["modelo", "marca", "año"]

#-------------------------------------------------------------------------------------------------------------------------------
#moto

class Motor(models.Model):
    motor = models.CharField(max_length=50)
    def __str__(self):
        return self.motor
class Freno(models.Model):
    freno = models.CharField(max_length=50)
    def __str__(self):
        return self.freno

class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    tipo_motor = models.ForeignKey(Motor, on_delete=models.CASCADE, null=True, default=None)
    tipo_freno = models.ForeignKey(Freno, on_delete=models.CASCADE, null=True, default=None)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}/ año {}".format(self.marca, self.modelo, self.año)

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"
        ordering = ["modelo", "marca", "año"]



#-------------------------------------------------------------------------------------------------------------------------------
#compra
class Metodo_de_pago(models.Model):
    metodo = models.CharField(max_length=50)

    def __str__(self):
        return self.metodo

class Compra(models.Model):
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE, null=True, default=None)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, default=None)
    camioneta = models.ForeignKey(Camioneta, on_delete=models.CASCADE, null=True, default=None)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    metodoPago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.usuario} - {self.automovil} - {self.metodoPago}"

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ["usuario"]
#-------------------------------------------------------------------------------------------------------------------------------
#reseña

class Nro_Puntuacion(models.Model):
    nro_puntuacion = models.CharField(max_length=20)

    def __str__(self):
        return self.nro_puntuacion

class Reseña(models.Model):
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE, null=True, blank=True)
    camioneta = models.ForeignKey(Camioneta, on_delete=models.CASCADE, null=True, blank=True)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.ForeignKey(Nro_Puntuacion, on_delete=models.CASCADE, null=True, default=None)
    contenido = models.TextField()

    def __str__(self):
        return "{} - {} estrellas".format(self.usuario, self.puntuacion)

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["usuario", "puntuacion"]

