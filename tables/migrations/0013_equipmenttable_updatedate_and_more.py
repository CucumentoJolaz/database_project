# Generated by Django 4.0 on 2022-02-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0012_remove_rawmaterialstable_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmenttable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='measurementunittable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='organisationtable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rawmaterialstable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='statustable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subcomponentstable',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
