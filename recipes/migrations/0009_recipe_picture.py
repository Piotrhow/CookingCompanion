# Generated by Django 4.0.3 on 2022-04-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(default='profile_def.jpg', upload_to='recipe_images'),
        ),
    ]
