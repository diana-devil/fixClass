# Generated by Django 3.1.1 on 2020-10-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0011_auto_20201028_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_fix',
            name='text_flag',
            field=models.CharField(default='未维修', max_length=20),
        ),
    ]
