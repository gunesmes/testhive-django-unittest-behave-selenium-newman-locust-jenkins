# Generated by Django 2.1.7 on 2020-05-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20180923_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
