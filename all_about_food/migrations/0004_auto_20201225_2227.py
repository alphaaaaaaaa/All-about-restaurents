# Generated by Django 3.1 on 2020-12-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_about_food', '0003_auto_20201225_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurent',
            name='image',
            field=models.ImageField(upload_to='img/restaurents'),
        ),
    ]
