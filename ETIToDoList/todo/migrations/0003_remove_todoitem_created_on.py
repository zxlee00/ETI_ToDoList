# Generated by Django 2.1 on 2019-12-17 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='created_on',
        ),
    ]