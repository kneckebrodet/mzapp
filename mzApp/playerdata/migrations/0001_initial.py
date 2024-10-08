# Generated by Django 5.1 on 2024-08-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('born', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('stamina', models.IntegerField()),
                ('play_intelligence', models.IntegerField()),
                ('passing', models.IntegerField()),
                ('shooting', models.IntegerField()),
                ('heading', models.IntegerField()),
                ('keeping', models.IntegerField()),
                ('ball_control', models.IntegerField()),
                ('tackling', models.IntegerField()),
                ('aerial_passing', models.IntegerField()),
                ('set_plays', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('form', models.IntegerField()),
            ],
        ),
    ]
