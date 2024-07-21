from django.contrib import admin
# Register your models here.
from entidades.models import *


admin.site.register(Automovil)
admin.site.register(Camioneta)
admin.site.register(Moto)
admin.site.register(Reseña)
admin.site.register(Compra)