# Generated by Django 3.1 on 2020-08-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0011_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
