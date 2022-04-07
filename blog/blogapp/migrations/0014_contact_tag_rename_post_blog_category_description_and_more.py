# Generated by Django 4.0.3 on 2022-04-07 04:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0013_alter_postimages_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_number', models.BigIntegerField()),
                ('messages', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/category/images/'),
        ),
    ]