# Generated by Django 3.2.8 on 2021-10-12 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0018_excelfile_additionalinfo'),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='equipmenttable',
            name='parentFolder',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.excelfolder'),
        ),
        migrations.AlterField(
            model_name='rawmaterialstable',
            name='parentFolder',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.excelfolder'),
        ),
        migrations.AlterField(
            model_name='subcomponentstable',
            name='parentFolder',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.excelfolder'),
        ),
        migrations.AlterField(
            model_name='equipmenttable',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.provider'),
        ),
        migrations.AlterField(
            model_name='rawmaterialstable',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.provider'),
        ),
    ]
