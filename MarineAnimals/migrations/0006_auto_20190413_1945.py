# Generated by Django 2.0 on 2019-04-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarineAnimals', '0005_animal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]