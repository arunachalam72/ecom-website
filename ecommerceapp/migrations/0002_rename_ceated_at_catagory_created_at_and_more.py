# Generated by Django 5.0.2 on 2024-07-19 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='ceated_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ceated_at',
            new_name='created_at',
        ),
    ]
