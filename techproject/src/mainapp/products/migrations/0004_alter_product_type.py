# Generated by Django 3.2.4 on 2021-06-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
