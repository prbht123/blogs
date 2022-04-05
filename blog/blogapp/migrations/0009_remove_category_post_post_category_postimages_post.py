# Generated by Django 4.0.3 on 2022-04-05 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_remove_postimages_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='blogapp.category'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='image_posts', to='blogapp.post'),
        ),
    ]