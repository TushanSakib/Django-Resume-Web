# Generated by Django 4.2.7 on 2023-11-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_image_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='product/image/'),
        ),
    ]
