# Generated by Django 4.0.3 on 2022-04-10 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_alter_estudiantes_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]