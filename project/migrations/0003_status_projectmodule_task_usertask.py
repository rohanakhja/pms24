# Generated by Django 5.0.2 on 2024-02-28 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectteam'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(choices=[('Not-started', 'Not-started'), ('In-progress', 'In-progress'), ('Testing', 'Testing'), ('Completed', 'Completed')], max_length=100)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='ProjectModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('estimated_hours', models.PositiveIntegerField()),
                ('startDate', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.status')),
            ],
            options={
                'db_table': 'project_module',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100)),
                ('description', models.TextField()),
                ('totalMinutes', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('project_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectmodule')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.status')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_task',
            },
        ),
    ]
