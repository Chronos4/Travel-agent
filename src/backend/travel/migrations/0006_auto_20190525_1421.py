# Generated by Django 2.1.7 on 2019-05-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_destination_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination_comment',
            name='user',
        ),
        migrations.AddField(
            model_name='destination_comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='destination_comment',
            name='name',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
