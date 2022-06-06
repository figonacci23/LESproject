# Generated by Django 4.0.4 on 2022-06-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0003_remove_zone_layout_delete_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='direction',
            field=models.CharField(choices=[('VE', 'Vertical'), ('HO', 'Horizontal')], db_column='Direction', default=1, max_length=2, verbose_name='Direction'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='x',
            field=models.IntegerField(db_column='Abscissa', default=1, verbose_name='Abscissa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='y',
            field=models.IntegerField(db_column='Ordiante', default=1, verbose_name='Ordiante'),
            preserve_default=False,
        ),
    ]
