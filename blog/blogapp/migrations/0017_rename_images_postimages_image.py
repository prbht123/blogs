# Generated by Django 4.0.3 on 2022-04-07 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_rename_image_postimages_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimages',
            old_name='images',
            new_name='image',
        ),
    ]
