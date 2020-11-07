# Generated by Django 3.1.1 on 2020-10-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0015_auto_20201028_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_fix',
            name='f_flag',
            field=models.BooleanField(choices=[(1, '已维修'), (0, '未维修')], default=0, verbose_name='维修状态'),
        ),
    ]