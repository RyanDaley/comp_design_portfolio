# Generated by Django 4.2.4 on 2024-01-14 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_address_author_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
    ]
