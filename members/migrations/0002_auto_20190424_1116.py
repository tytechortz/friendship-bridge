# Generated by Django 2.0.13 on 2019-04-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='outter_core_member',
            new_name='outer_core_member',
        ),
    ]