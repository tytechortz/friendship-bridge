# Generated by Django 2.0.13 on 2019-04-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20190424_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('core', 'Core Member'), ('outer-core', 'Outer Core'), ('events-only', 'Events Only')], max_length=11),
        ),
    ]
