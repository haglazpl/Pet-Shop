# Generated by Django 5.0.6 on 2024-05-21 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0002_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='petstore.subcategory'),
        ),
    ]
