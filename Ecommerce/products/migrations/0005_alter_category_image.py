# Generated by Django 5.1.6 on 2025-03-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='static/images/laptops.png', upload_to='Categories/%Y/%m/%d/%h/%M/'),
        ),
    ]
