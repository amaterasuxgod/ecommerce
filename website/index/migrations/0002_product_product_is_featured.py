# Generated by Django 3.2.3 on 2021-06-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_is_featured',
            field=models.BooleanField(default=False, verbose_name='Product featured'),
        ),
    ]