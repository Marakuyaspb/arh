# Generated by Django 4.1.13 on 2024-06-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renew', '0005_alter_case_main_img_alter_case_main_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='engeneer',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Инженер'),
        ),
    ]