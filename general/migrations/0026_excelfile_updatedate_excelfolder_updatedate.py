# Generated by Django 4.0 on 2022-02-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0025_remove_excelfile_parentfolder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelfile',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='excelfolder',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
