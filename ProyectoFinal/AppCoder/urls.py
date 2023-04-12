from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.urls import include, path

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    #------Pasth login, logout, registo y avatar
    path('login',views.login_request, name='Login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil',views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name= 'AgregarAvatar'),
    #--------------Libros-----------------------
    path('libro',views.texto,name='Libro'),
    path('formularioLibro',views.formularioLibro,name='FormularioLibro'),
    path('leerLibro',views.leerLibro,name='LeerLibro'),
    path('eliminarLibro/<libro_titulo>/',views.eliminarLibro,name='EliminarLibro'),
    path('editarLibro/<libro_titulo>/',views.editarLibro,name='EditarLibro'),
    path('busquedaLibro',views.busquedaLibro,name='BusquedaLibro'),
    path('buscar/',views.buscar),
#--------------Propietario-----------------------
    path('propietario',views.propietario,name='Propietario'),
    path('formularioPropietario',views.formularioPropietario,name='FormularioPropietario'),
    path('leerPropietario',views.leerPropietario,name='LeerPropietario'), 
    path('eliminarPropietario/<propietario_nombre>/',views.eliminarPropietario,name='EliminarPropietario'),
    path('editarPropietario/<propietario_nombre>/',views.editarPropietario,name='EditarPropietario'),
#--------------Autor-----------------------
    path('autor',views.autor,name='Autor'),
    path('formularioAutor',views.formularioAutor,name='FormularioAutor'),
    path('leerAutor',views.leerAutor,name='LeerAutor'), 
    path('eliminarAutor/<autor_nombre>/',views.eliminarAutor,name='EliminarAutor'),
    path('editarAutor/<autor_nombre>/',views.eliminarAutor,name='EditarAutor'),

]