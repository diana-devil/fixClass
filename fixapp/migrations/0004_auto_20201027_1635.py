# Generated by Django 3.1.1 on 2020-10-27 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0003_fix_class_is_deleta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fix_class',
            old_name='is_deleta',
            new_name='is_delete',
        ),
    ]
