# Generated by Django 4.1.7 on 2023-03-29 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230329_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='decription',
            new_name='description',
        ),
    ]
