# Generated by Django 5.0 on 2023-12-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0010_rename_title_message_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='message',
            name='venue',
        ),
    ]
