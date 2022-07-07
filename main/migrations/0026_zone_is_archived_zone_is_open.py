# Generated by Django 4.0.6 on 2022-07-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_pricetable_arquived_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='is_archived',
            field=models.BooleanField(db_column='IsArchived', default=False, verbose_name='Archived'),
        ),
        migrations.AddField(
            model_name='zone',
            name='is_open',
            field=models.BooleanField(db_column='IsOpen', default=False, verbose_name='Open'),
        ),
    ]