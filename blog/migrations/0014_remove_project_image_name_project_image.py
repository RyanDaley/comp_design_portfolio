# Generated by Django 4.2.4 on 2024-01-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_name',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
