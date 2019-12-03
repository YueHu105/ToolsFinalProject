# Generated by Django 2.2.7 on 2019-12-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrels',
            fields=[
                ('Latitude', models.DecimalField(decimal_places=10, max_digits=21)),
                ('Longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('Unique_Squirrel_ID', models.TextField(primary_key=True, serialize=False)),
                ('Shift', models.TextField()),
                ('Date', models.IntegerField()),
                ('Age', models.TextField()),
                ('Primary_Fur_Color', models.TextField()),
                ('Location', models.TextField()),
                ('Specific_Location', models.TextField()),
                ('Running', models.IntegerField()),
                ('Chasing', models.IntegerField()),
                ('Climbing', models.IntegerField()),
                ('Eating', models.IntegerField()),
                ('Foraging', models.IntegerField()),
                ('Other_Activities', models.TextField()),
                ('Kuks', models.IntegerField()),
                ('Quaas', models.IntegerField()),
                ('Moans', models.IntegerField()),
                ('Tail_flags', models.IntegerField()),
                ('Tail_twitches', models.IntegerField()),
                ('Approaches', models.IntegerField()),
                ('Indifferent', models.IntegerField()),
                ('Runs_from', models.IntegerField()),
            ],
        ),
    ]