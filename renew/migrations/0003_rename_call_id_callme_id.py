# Generated by Django 4.1.13 on 2024-06-13 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renew', '0002_remove_callme_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callme',
            old_name='call_id',
            new_name='id',
        ),
    ]
