# Generated by Django 3.1 on 2020-08-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0008_auto_20200820_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]