# Generated by Django 4.0 on 2022-01-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0022_alter_excelfolder_parentfolder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfolder',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='excelfolder',
            name='path',
            field=models.CharField(blank=True, default='ghost', max_length=300),
        ),
        migrations.AlterField(
            model_name='excelfolder',
            name='tableName',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
