# Generated by Django 3.1.5 on 2021-01-13 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantrace', '0002_remove_trace_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='can_id',
            new_name='can_id_decimal',
        ),
    ]
