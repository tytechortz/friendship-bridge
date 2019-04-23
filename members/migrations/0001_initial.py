# Generated by Django 2.0.13 on 2019-04-23 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=12)),
                ('phone2', models.CharField(max_length=12)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.TextField()),
                ('zipcode', models.CharField(max_length=5)),
                ('notes', models.TextField()),
                ('core_member', models.BooleanField()),
                ('outter_core_member', models.BooleanField()),
                ('events_only_member', models.BooleanField()),
                ('last_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
