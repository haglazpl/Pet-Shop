# Generated by Django 5.0.6 on 2024-05-21 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0005_alter_category_options_subcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
