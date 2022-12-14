# Generated by Django 4.1.2 on 2022-10-24 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_rename_user_thing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thing',
            options={},
        ),
        migrations.AlterModelManagers(
            name='thing',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='thing',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='email',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='password',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='username',
        ),
    ]
