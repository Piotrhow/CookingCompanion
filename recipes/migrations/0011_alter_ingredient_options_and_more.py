# Generated by Django 4.0.4 on 2022-04-29 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ingredientcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Ingredient categories'},
        ),
    ]