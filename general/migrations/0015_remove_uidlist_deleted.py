# Generated by Django 3.1.2 on 2020-12-03 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_auto_20201203_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uidlist',
            name='deleted',
        ),
    ]