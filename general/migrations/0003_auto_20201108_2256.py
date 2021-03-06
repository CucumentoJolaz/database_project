# Generated by Django 3.1.2 on 2020-11-08 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20201108_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmenttable',
            name='parentFolder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='general.equipmenttable'),
        ),
        migrations.AddField(
            model_name='excelfolder',
            name='parentFolder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='general.excelfolder'),
        ),
        migrations.AddField(
            model_name='rawmaterialstable',
            name='parentFolder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='general.rawmaterialstable'),
        ),
        migrations.AddField(
            model_name='subcomponentstable',
            name='parentFolder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='general.subcomponentstable'),
        ),
    ]
