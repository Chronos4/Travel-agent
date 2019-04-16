# Generated by Django 2.1.7 on 2019-04-15 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='places_been',
        ),
        migrations.RemoveField(
            model_name='user',
            name='places_to',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to='accounts.User'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='accounts.User'),
        ),
    ]
