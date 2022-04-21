# Generated by Django 4.0.4 on 2022-04-12 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_ingredientcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredientcategory'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredientunit'),
        ),
    ]