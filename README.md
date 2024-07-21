#Proyecto Final - Pagina de compra-venta de vehículos

##Descripcion del proyecto

El objetivo principal de esta página es simular la funcionalidad de una pagina de compra-venta de vehículos, permitiendo a los usuarios registrar sus cuentas, comprar y vender vehículos, y dejar reseñas de los vehículos adquiridos. El proyecto fue desarrollado utilizando Django y Python, y abarca diferentes aspectos del desarrollo web, desde la gestión de usuarios hasta la manipulación de bases de datos y la implementación de una interfaz de usuario funcional y atractiva.

##objetivo funccional

El objetivo principal de esta página web es simular el funcionamiento de un concesionario de automóviles, proporcionando a los usuarios una plataforma donde pueden explorar, comprar y vender vehículos. La plataforma incluye las siguientes funcionalidades clave:

1- Registro e Inicio de Sesión de Usuarios: Permite a los usuarios crear una cuenta y acceder a la plataforma.
2- Visualización de Vehículos: Los usuarios pueden ver una lista completa de automóviles, camionetas y motos disponibles, con detalles específicos de cada uno.
3- Compra de Vehículos: Los usuarios pueden comprar vehículos a través de la plataforma, eligiendo entre diferentes métodos de pago.
4- Publicación de Reseñas: Los usuarios pueden escribir y publicar reseñas de los vehículos que han comprado, ayudando a otros usuarios en sus decisiones de compra.
5- Gestión de Vehículos: Los usuarios pueden añadir nuevos vehículos a la plataforma para su venta y gestionar sus publicaciones.

##Modelos

### Usuario

- Nombre de usuario
- Nombre
- Apellido
- Email
- Contraseña

### Automóvil

- Marca
- Modelo
- Año
- Precio
- Cantidad de pasajeros (2, 5 o 8)
- Vendedor

### Camioneta

- Marca
- Modelo
- Año
- Precio
- Tracción (4x2 o 4x4)
- Tipo de cabina (cabina simple o cabina doble)
- Vendedor

### Moto

- Marca
- Modelo
- Año
- Precio
- Tipo de motor (2 tiempos o 4 tiempos)
- Tipo de freno (tambor o disco)
- Vendedor

### Compra

- Automóvil (opcional)
- Camioneta (opcional)
- Moto (opcional)
- Usuario
- Método de pago (efectivo, tarjeta de crédito, tarjeta de débito, transferencia bancaria, PayPal, criptomonedas)

### Reseña

- Automóvil (opcional)
- Camioneta (opcional)
- Moto (opcional)
- Usuario
- Puntuación (1 a 5 estrellas)
- Contenido


##Usuarios

###Usuario Administrador

path: /admin/
Nombre de usuario: Administrador
Contraseña: 1234

###Demas usuarios:

1. **Usuario 1**:
   - Nombre de usuario: juan123
   - Nombre: Juan
   - Apellido: Pérez
   - Email: juan.perez@example.com
   - Contraseña: Renzooo20088

2. **Usuario 2**:
   - Nombre de usuario: maria456
   - Nombre: María
   - Apellido: García
   - Email: maria.garcia@example.com
   - Contraseña: Renzooo20088

3. **Usuario 3**:
   - Nombre de usuario: carlos789
   - Nombre: Carlos
   - Apellido: López
   - Email: carlos.lopez@example.com
   - Contraseña: Renzooo20088

4. **Usuario 4**:
   - Nombre de usuario: ana111
   - Nombre: Ana
   - Apellido: Rodríguez
   - Email: ana.rodriguez@example.com
   - Contraseña: Renzooo20088

5. **Usuario 5**:
   - Nombre de usuario: pedro222
   - Nombre: Pedro
   - Apellido: Fernández
   - Email: pedro.fernandez@example.com
   - Contraseña: Renzooo20088

6. **Usuario 6**:
   - Nombre de usuario: lucia333
   - Nombre: Lucía
   - Apellido: Martínez
   - Email: lucia.martinez@example.com
   - Contraseña: Renzooo20088
  
7. **Usuario 7**:
   - Nombre de usuario: pablo666
   - Nombre: Pablo
   - Apellido: Ruiz
   - Email: pablo.ruiz@example.com
   - Contraseña: Renzooo20088


##Video

https://drive.google.com/file/d/1xT7CH8jvWQi_LiyuOJ505sT44KA2Jjgg/view?usp=drivesdk
