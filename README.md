# ProyectoFinal_Margarida
Proyecto final desarrollado en Python usando el framework Django. 
El proyecto es una pagina web destinada a una biblioteca digital, en esta se va a mostrar la informacion que tenemos almacenada en la base de datos mediante distintas vistas.

1. Moverse a la carpeta del proyecto ejecutando:

```
cd ProyectoFinal
```

2. Ejecutar:

```
python manage.py runserver
```
 
3.Abrir en el navegador la siguiente direccion:

 ```
 http://localhost:8000/AppCoder
 ```
 Una vez iniciada la aplicación se podra iniciar sesion como admin o bien se podra registrar un nuevo usuario.
 Al ingresar nos encontraremos en el inicio donde se podra navegar por las distintas vistas disponibles:
 
* Libros que nos permite ver el listado de Libros ingresados en nuestra base, con el botón "Agregar" podemos cargar los datos de un nuevo libro o tambien podremos "Borrar" o "Editar" cualquiera de nuestros registros. 
* Propietarios nos permite ver los dueños de los libros ingresados los cuales al igual que en libros podemos "Agregar", "Editar" o "Borrar".
* Autores nos permite ver el listado de autores delos libros ingresados, los cuales tambien podermos "Agregar", "Editar" o "Borrar".
* Buscar Libro nos permite buscar en nuestra base de datos de los libros que tenemos registrados.
* Botón desplegable con nuestro Avatar y nombre de Usuario:
    - Editar Perfil: Nos permite actualizar los datos del usuario.
    - Agregar Avatar: Nos permite agregar o editar nuestro Avatar.
    - Cerrar Sesión: Finaliza la sesión.
    
4. Ingresar como administrador

 ```
 http://localhost:8000/admin
 ```
Usuario: ProyectoFinal
Clave: Coder34670
