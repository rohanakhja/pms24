# Generated by Django 5.0.3 on 2024-03-22 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_usertask_bug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertask',
            name='bug',
        ),
    ]