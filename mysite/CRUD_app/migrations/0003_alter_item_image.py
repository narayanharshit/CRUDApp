# Generated by Django 4.2.6 on 2023-10-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_app', '0002_alter_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='items/'),
        ),
    ]
