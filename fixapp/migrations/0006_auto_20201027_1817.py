# Generated by Django 3.1.1 on 2020-10-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0005_auto_20201027_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='fix_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('stu_id', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('class_id', models.CharField(max_length=20)),
                ('msg', models.TextField()),
                ('flag', models.CharField(max_length=10)),
                ('is_delete', models.BooleanField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='class_fix',
        ),
    ]
