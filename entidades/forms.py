from django import forms
from .models import *

from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ReseñaForm(forms.Form):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.none(), required=False)
    camioneta = forms.ModelChoiceField(queryset=Camioneta.objects.none(), required=False)
    moto = forms.ModelChoiceField(queryset=Moto.objects.none(), required=False)
    puntuacion = forms.ModelChoiceField(queryset=Nro_Puntuacion.objects.all(), required=True)
    contenido = forms.CharField(required=True)

#asegurarse que los usuarios solo dejen reseñas en los autos adquiridos

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReseñaForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['automovil'].queryset = Automovil.objects.filter(compra__usuario=user)
            self.fields['camioneta'].queryset = Camioneta.objects.filter(compra__usuario=user)
            self.fields['moto'].queryset = Moto.objects.filter(compra__usuario=user)

#asegurarse que el usuario solo selecccione un auto

    def clean(self):
        cleaned_data = super().clean()
        automovil = cleaned_data.get("automovil")
        camioneta = cleaned_data.get("camioneta")
        moto = cleaned_data.get("moto")

        if sum(bool(x) for x in [automovil, camioneta, moto]) != 1:
            raise forms.ValidationError("Debe seleccionar un solo tipo de vehículo.")
        return cleaned_data

class CompraForm(forms.Form):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.all(), required=False)
    camioneta = forms.ModelChoiceField(queryset=Camioneta.objects.all(), required=False)
    moto = forms.ModelChoiceField(queryset=Moto.objects.all(), required=False)
    metodoPago = forms.ModelChoiceField(queryset=Metodo_de_pago.objects.all(), required=True)

#asegurarse que el usuario solo selecccione un auto

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CompraForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        automovil = cleaned_data.get("automovil")
        camioneta = cleaned_data.get("camioneta")
        moto = cleaned_data.get("moto")

        if sum(bool(x) for x in [automovil, camioneta, moto]) != 1:
            raise forms.ValidationError("Debe seleccionar un solo tipo de vehículo.")
        
        if automovil and Compra.objects.filter(automovil=automovil, usuario=self.user).exists():
            raise forms.ValidationError("Ya ha comprado este automóvil.")
        if camioneta and Compra.objects.filter(camioneta=camioneta, usuario=self.user).exists():
            raise forms.ValidationError("Ya ha comprado esta camioneta.")
        if moto and Compra.objects.filter(moto=moto, usuario=self.user).exists():
            raise forms.ValidationError("Ya ha comprado esta moto.")

        return cleaned_data



class UserEditForm(UserChangeForm):
    username = forms.CharField(label="Nombre de usuario", max_length=50, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["username","email", "first_name", "last_name"]

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "password1", "password2"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)