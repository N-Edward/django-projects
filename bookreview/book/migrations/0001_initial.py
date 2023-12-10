# Generated by Django 4.2.7 on 2023-11-24 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=3000)),
                ('author', models.CharField(max_length=60)),
                ('upload_date', models.TimeField(default=django.utils.timezone.now)),
                ('book_cover', models.ImageField(upload_to='')),
            ],
        ),
    ]
