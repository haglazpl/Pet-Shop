# Generated by Django 5.0.6 on 2024-05-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0008_remove_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]