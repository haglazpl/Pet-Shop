# Generated by Django 5.0.6 on 2024-05-30 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0007_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
