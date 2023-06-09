# Generated by Django 4.1.7 on 2023-04-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='creador',
            name='apellidoaut',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='texto',
            name='disponible',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='texto',
            name='edicion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='texto',
            name='editorial',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
