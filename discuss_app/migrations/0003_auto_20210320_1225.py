# Generated by Django 3.1.7 on 2021-03-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss_app', '0002_auto_20210320_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='discusstheme',
            name='another_side_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discusstheme',
            name='max_n_of_member',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='discusstheme',
            name='one_side_count',
            field=models.IntegerField(default=0),
        ),
    ]
