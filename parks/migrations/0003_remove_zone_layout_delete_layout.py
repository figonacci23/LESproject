# Generated by Django 4.0.4 on 2022-06-01 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0002_alter_park_friday_end_alter_park_friday_start_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='layout',
        ),
        migrations.DeleteModel(
            name='Layout',
        ),
    ]
