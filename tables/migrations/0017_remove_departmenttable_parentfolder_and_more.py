# Generated by Django 4.0 on 2022-02-15 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_departmenttable_alter_equipmenttable_uid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmenttable',
            name='parentFolder',
        ),
        migrations.RemoveField(
            model_name='documenttable',
            name='parentFolder',
        ),
        migrations.RemoveField(
            model_name='documenttypetable',
            name='parentFolder',
        ),
    ]
