# Generated by Django 4.1.7 on 2023-04-02 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreaut', models.CharField(max_length=20)),
                ('apellidoaut', models.CharField(max_length=40)),
                ('tituloLibro', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('tituloLibro', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloLibro', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('edicion', models.IntegerField()),
                ('genero', models.CharField(max_length=40)),
                ('editorial', models.CharField(max_length=40)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
