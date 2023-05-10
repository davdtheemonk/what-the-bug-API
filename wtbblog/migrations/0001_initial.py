# Generated by Django 4.0.2 on 2023-05-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('timetoread', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('post', models.TextField(blank=True)),
            ],
        ),
    ]
