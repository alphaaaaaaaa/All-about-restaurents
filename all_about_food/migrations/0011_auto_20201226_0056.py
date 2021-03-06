# Generated by Django 3.1 on 2020-12-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_about_food', '0010_restaurent_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='img/dishes/'),
        ),
        migrations.AlterField(
            model_name='restaurent',
            name='image',
            field=models.ImageField(upload_to='img/restaurents/'),
        ),
    ]
