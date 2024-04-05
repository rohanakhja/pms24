# Generated by Django 5.0.3 on 2024-03-22 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_remove_usertask_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='bug',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.bug'),
            preserve_default=False,
        ),
    ]