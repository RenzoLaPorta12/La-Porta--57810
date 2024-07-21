from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Login, Logout, and Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #leer avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "entidades/home.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
        else:
            miForm = RegistroForm()
    else:
        miForm = RegistroForm()
    return render(request, "entidades/registro.html", {"form": miForm})


#-------------------------------------------------------------------------------------------------------------------------------
#edicion de perfil -- agregar avatar


@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.username = miForm.cleaned_data.get("username")
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]

            #borrar avatares
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #enviar imagen a home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
        
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})


#-------------------------------------------------------------------------------------------------------------------------------
# Reseña
@login_required
def reseña(request):
    contexto = {"Reseña": Reseña.objects.all()}
    return render(request, "entidades/reseña.html", contexto)

@login_required
def reseñaForm(request):
    if request.method == "POST":
        miForm = ReseñaForm(request.POST, user=request.user)
        if miForm.is_valid():
            reseña_automovil = miForm.cleaned_data.get("automovil")
            reseña_camioneta = miForm.cleaned_data.get("camioneta")
            reseña_moto = miForm.cleaned_data.get("moto")
            reseña_puntuacion = miForm.cleaned_data.get("puntuacion")
            reseña_contenido = miForm.cleaned_data.get("contenido")

            #verificar si el usuario compro el vehículo
            if reseña_automovil and Compra.objects.filter(automovil=reseña_automovil, usuario=request.user).exists():
                reseña = Reseña(automovil=reseña_automovil, usuario=request.user, puntuacion=reseña_puntuacion, contenido=reseña_contenido)
            elif reseña_camioneta and Compra.objects.filter(camioneta=reseña_camioneta, usuario=request.user).exists():
                reseña = Reseña(camioneta=reseña_camioneta, usuario=request.user, puntuacion=reseña_puntuacion, contenido=reseña_contenido)
            elif reseña_moto and Compra.objects.filter(moto=reseña_moto, usuario=request.user).exists():
                reseña = Reseña(moto=reseña_moto, usuario=request.user, puntuacion=reseña_puntuacion, contenido=reseña_contenido)
            
            reseña.save()
            contexto = {"Reseña": Reseña.objects.all()}
            return render(request, "entidades/reseña.html", contexto)
    else:
        miForm = ReseñaForm(user=request.user)
    return render(request, "entidades/reseñaForm.html", {"form": miForm})

class ReseñaDelete(DeleteView, LoginRequiredMixin):
    model = Reseña
    success_url = reverse_lazy("reseña")

#-------------------------------------------------------------------------------------------------------------------------------
# Vender - Automovil


@login_required
def buscarAutomovil(request):
    return render(request, "entidades/buscarAutomovil.html")
@login_required
def encontrarAutomovil(request):
    if request.GET.get("buscar"):
        patron = request.GET["buscar"]
        autos = Automovil.objects.filter(marca__icontains=patron)
        contexto = {'automovil_list': autos}
    else:
        contexto = {'automovil_list': Automovil.objects.all()}
    return render(request, "entidades/automovil_list.html", contexto)

class AutomovilList(ListView, LoginRequiredMixin):
    model = Automovil

class AutomovilCreate(LoginRequiredMixin, CreateView):
    model = Automovil
    fields = ["marca", "modelo", "año", "precio", "pasajeros"]

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("vender")

class AutomovilUpdate(UpdateView, LoginRequiredMixin):
    model = Automovil
    fields = ["marca", "modelo", "año", "precio", "pasajeros"]
    success_url = reverse_lazy("lista_de_autos")

class AutomovilDelete(DeleteView, LoginRequiredMixin):
    model = Automovil
    success_url = reverse_lazy("lista_de_autos")

#-------------------------------------------------------------------------------------------------------------------------------
# Vender - Camioneta

@login_required
def buscarCamioneta(request):
    return render(request, "entidades/buscarAutomovil.html")
@login_required
def encontrarCamioneta(request):
    if request.GET.get("buscar"):
        patron = request.GET["buscar"]
        camioneta = Camioneta.objects.filter(marca__icontains=patron)
        contexto = {'camioneta_list': camioneta}
    else:
        contexto = {'camioneta_list': Camioneta.objects.all()}
    return render(request, "entidades/camioneta_list.html", contexto)

class CamionetaList(ListView, LoginRequiredMixin):
    model = Camioneta

class CamionetaCreate(LoginRequiredMixin, CreateView):
    model = Camioneta
    fields = ["marca", "modelo", "año", "precio", "traccion", "tipo_cabina"]

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("vender")

class CamionetaUpdate(UpdateView, LoginRequiredMixin):
    model = Camioneta
    fields = ["marca", "modelo", "año", "precio", "traccion", "tipo_cabina"]
    success_url = reverse_lazy("lista_de_camionetas")

class CamionetaDelete(DeleteView, LoginRequiredMixin):
    model = Camioneta
    success_url = reverse_lazy("lista_de_camionetas")

#-------------------------------------------------------------------------------------------------------------------------------
# Vender - Moto


@login_required
def buscarMoto(request):
    return render(request, "entidades/buscarMoto.html")
@login_required
def encontrarMoto(request):
    if request.GET.get("buscar"):
        patron = request.GET["buscar"]
        motos = Moto.objects.filter(marca__icontains=patron)
        contexto = {'moto_list': motos}
    else:
        contexto = {'moto_list': Moto.objects.all()}
    return render(request, "entidades/moto_list.html", contexto)

class MotoList(ListView, LoginRequiredMixin):
    model = Moto

class MotoCreate(LoginRequiredMixin, CreateView):
    model = Moto
    fields = ["marca", "modelo", "año", "precio", "tipo_motor", "tipo_freno"]

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("vender")

class MotoUpdate(UpdateView, LoginRequiredMixin):
    model = Moto
    fields = ["marca", "modelo", "año", "precio", "tipo_motor", "tipo_freno"]
    success_url = reverse_lazy("lista_de_motos")

class MotoDelete(DeleteView, LoginRequiredMixin):
    model = Moto
    success_url = reverse_lazy("lista_de_motos")



#-------------------------------------------------------------------------------------------------------------------------------
# Comprar
@login_required
def comprar(request):
    return render(request, "entidades/comprar.html")

@login_required
def compraForm(request):
    if request.method == "POST":
        miForm = CompraForm(request.POST, user=request.user)
        if miForm.is_valid():
            compra_automovil = miForm.cleaned_data.get("automovil")
            compra_moto = miForm.cleaned_data.get("moto")
            compra_camioneta = miForm.cleaned_data.get("camioneta")
            compra_metodoPago = miForm.cleaned_data.get("metodoPago")
            compra = Compra(automovil=compra_automovil,moto=compra_moto,camioneta=compra_camioneta, usuario=request.user, metodoPago=compra_metodoPago)
            compra.save()
            contexto = {"Compra": Compra.objects.filter(usuario=request.user)}
            return render(request, "entidades/comprar.html", contexto)
    else:
        miForm = CompraForm()
    return render(request, "entidades/compraForm.html", {"form": miForm})


#-------------------------------------------------------------------------------------------------------------------------------
# Añadidos
def home2(request):
    return render(request, "entidades/home2.html")
@login_required
def home(request):
    return render(request, "entidades/home.html")
@login_required
def about(request):
    return render(request, "entidades/about.html")
@login_required
def terminos(request):
    return render(request, "entidades/terminos.html")
@login_required
def privacidad(request):
    return render(request, "entidades/privacidad.html")
@login_required
def contact(request):
    return render(request, "entidades/contact.html")
@login_required
def confirmLogout(request):
    return render(request, "entidades/confirmLogout.html")
@login_required
def vender(request):
    return render(request, "entidades/vender.html")
@login_required
def seleccion(request):
    return render(request, "entidades/seleccion.html")
@login_required
def historial(request):
    contexto = {"Compra": Compra.objects.filter(usuario=request.user)}
    return render(request, "entidades/historial.html", contexto)