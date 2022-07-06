# Generated by Django 4.0.4 on 2022-07-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_car_registration_alter_car_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(db_column='Brand', max_length=20, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(db_column='Model', max_length=20, verbose_name='Model'),
        ),
    ]