# Generated by Django 4.1.7 on 2023-04-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_texto_imagen_alter_creador_apellidoaut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='disponible',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='texto',
            name='edicion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='texto',
            name='editorial',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
