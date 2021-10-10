# Generated by Django 3.1.2 on 2020-12-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_auto_20201202_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='fileFolder',
            field=models.ForeignKey(default=107, on_delete=django.db.models.deletion.PROTECT, to='general.excelfolder'),
        ),
        migrations.AlterField(
            model_name='excelfolder',
            name='parentFolder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='general.excelfolder'),
        ),
    ]
