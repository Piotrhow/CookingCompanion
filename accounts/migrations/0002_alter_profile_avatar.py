# Generated by Django 4.0.4 on 2022-05-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_def.jpg', upload_to='profile_images'),
        ),
    ]
