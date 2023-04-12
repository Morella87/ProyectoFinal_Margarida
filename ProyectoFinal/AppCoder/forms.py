from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Ingrese su email:')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:'' for k in fields}

class TextoFormulario(forms.Form):
    tituloLibro = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    edicion = forms.IntegerField()
    genero = forms.CharField(max_length=30)
    editorial = forms.CharField(max_length=40)
    disponible = forms.CharField(max_length=10)
    tapaLibro = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['tituloLibro', 'autor', 'edicion', 'genero', 'editorial', 'disponible', 'tapaLibro']
        help_text = {k:'' for k in fields}

class PropietarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    tituloLibro = forms.CharField(max_length=40)

class CreadorFormulario(forms.Form):
    nombreaut = forms.CharField(max_length=30)
    apellidoaut = forms.CharField(max_length=40)
    tituloLibro = forms.CharField(max_length=40)