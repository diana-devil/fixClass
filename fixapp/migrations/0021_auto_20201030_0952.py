# Generated by Django 3.1.1 on 2020-10-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0020_auto_20201029_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_fix',
            name='user',
        ),
        migrations.AlterField(
            model_name='class_fix',
            name='class_id',
            field=models.CharField(default='***', max_length=20, verbose_name='待维修班级'),
        ),
    ]
