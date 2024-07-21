from django.urls import path
from entidades.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Login, Logout, Registration
    path('login/', loginRequest, name="login"),
    path('confirmLogout/', confirmLogout, name="confirmLogout"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),


    #edicion de perfil -- avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/',CambiarClave.as_view() , name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
    


    # Añadidos
    path('', home, name="home"),
    path('home/', home2, name="home2"),
    path('about/', about, name="about"),
    path('terminos_de_uso/', terminos, name="terminos"),
    path('politicas_de_privacidad/', privacidad, name="privacidad"),
    path('contact/', contact, name="contact"),
    path('vender/', vender, name="vender"),
    path('seleccion/', seleccion, name="seleccion"),
    path('HistorialDeCompras/', historial, name="Historial"),

    # Reseña
    path('reseña/', reseña, name="reseña"),
    path('reseña_form/', reseñaForm, name="reseñaForm"),
    path('reseñaDelete/<int:pk>/', ReseñaDelete.as_view(), name="reseñaDelete"),

    # Vender - Automovil
    path('buscarAutomovil/', buscarAutomovil, name="buscarAutomovil"),
    path('encontrarAutomovil/', encontrarAutomovil, name="encontrarAutomovil"),
    path('lista_de_autos/', AutomovilList.as_view(), name="lista_de_autos"),
    path('vender/automovilCreate/', AutomovilCreate.as_view(), name="automovilCreate"),
    path('automovilUpdate/<int:pk>/', AutomovilUpdate.as_view(), name="automovilUpdate"),
    path('automovilDelete/<int:pk>/', AutomovilDelete.as_view(), name="automovilDelete"),
    
    # Vender - Camioneta
    path('buscarCamioneta/', buscarCamioneta, name="buscarCamioneta"),
    path('encontrarCamioneta/', encontrarCamioneta, name="encontrarCamioneta"),
    path('lista_de_camionetas/', CamionetaList.as_view(), name="lista_de_camionetas"),
    path('vender/camionetaCreate/', CamionetaCreate.as_view(), name="camionetaCreate"),
    path('camionetaUpdate/<int:pk>/', CamionetaUpdate.as_view(), name="camionetaUpdate"),
    path('camionetaDelete/<int:pk>/', CamionetaDelete.as_view(), name="camionetaDelete"),

    
    # Vender - Moto
    path('buscarMoto/', buscarMoto, name="buscarMoto"),
    path('encontrarMoto/', encontrarMoto, name="encontrarMoto"),
    path('lista_de_motos/', MotoList.as_view(), name="lista_de_motos"),
    path('vender/motoCreate/', MotoCreate.as_view(), name="motoCreate"),
    path('motoUpdate/<int:pk>/', MotoUpdate.as_view(), name="motoUpdate"),
    path('motoDelete/<int:pk>/', MotoDelete.as_view(), name="motoDelete"),
    
    
    # Comprar
    path('comprar/', comprar, name="comprar"),
    path('compra_form/', compraForm, name="compraForm"),
]
