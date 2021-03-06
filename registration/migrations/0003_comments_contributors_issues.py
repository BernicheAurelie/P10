# Generated by Django 3.2.5 on 2021-12-06 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user_id', to=settings.AUTH_USER_MODEL)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_id', to='registration.projects')),
                ('project_issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_issue_id', to='registration.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='registration.projects')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_project_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_project_user_id', to='registration.projects')),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_id', to='registration.issues')),
            ],
        ),
    ]
