# Generated by Django 4.0.2 on 2022-02-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtbblog', '0004_rename_blog_image_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
