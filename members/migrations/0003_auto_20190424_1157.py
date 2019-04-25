# Generated by Django 2.0.13 on 2019-04-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20190424_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='core_member',
        ),
        migrations.RemoveField(
            model_name='member',
            name='events_only_member',
        ),
        migrations.RemoveField(
            model_name='member',
            name='outer_core_member',
        ),
        migrations.AddField(
            model_name='member',
            name='member_type',
            field=models.TextField(blank=True),
        ),
    ]
