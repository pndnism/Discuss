# Generated by Django 3.1.7 on 2021-03-20 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('o', 'Open'), ('a', 'Active'), ('c', 'Closed')], max_length=2)),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discuss_app.themegenre')),
            ],
        ),
    ]
