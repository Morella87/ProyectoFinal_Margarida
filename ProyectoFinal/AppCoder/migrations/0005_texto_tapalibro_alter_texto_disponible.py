# Generated by Django 4.1.7 on 2023-04-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_remove_texto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='tapaLibro',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='texto',
            name='disponible',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
