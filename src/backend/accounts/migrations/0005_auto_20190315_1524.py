# Generated by Django 2.1.1 on 2019-03-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.DateField(),
        ),
    ]