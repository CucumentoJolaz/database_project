# Generated by Django 3.2.8 on 2021-10-13 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20211012_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmenttable',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.provider'),
        ),
        migrations.AlterField(
            model_name='rawmaterialstable',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.provider'),
        ),
    ]
