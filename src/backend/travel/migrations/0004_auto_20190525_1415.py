# Generated by Django 2.1.7 on 2019-05-25 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20190525_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination_comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='destination_comment',
            name='name',
        ),
    ]
