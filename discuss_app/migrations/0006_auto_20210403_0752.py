# Generated by Django 3.1.7 on 2021-04-03 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss_app', '0005_auto_20210403_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussside',
            old_name='another_side',
            new_name='side_claim',
        ),
        migrations.RenameField(
            model_name='discussside',
            old_name='another_side_count',
            new_name='side_count',
        ),
        migrations.RemoveField(
            model_name='discussside',
            name='one_side',
        ),
        migrations.RemoveField(
            model_name='discussside',
            name='one_side_count',
        ),
    ]
