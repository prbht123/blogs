# Generated by Django 4.0.3 on 2022-04-07 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_alter_category_image_alter_postimages_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimages',
            old_name='image',
            new_name='images',
        ),
    ]
