# Generated by Django 5.0.2 on 2024-03-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_status_projectmodule_task_usertask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertask',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]