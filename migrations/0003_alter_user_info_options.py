# Generated by Django 3.2.5 on 2021-10-20 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_user_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_info',
            options={'ordering': ['name']},
        ),
    ]