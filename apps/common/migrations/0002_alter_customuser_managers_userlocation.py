# Generated by Django 5.1.4 on 2024-12-11 14:41

import apps.common.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', apps.common.models.CustomObject()),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('langitude', models.FloatField()),
                ('home', models.CharField(max_length=200)),
                ('kv', models.CharField(max_length=200)),
                ('podyezd', models.CharField(max_length=200)),
                ('domofon_code', models.CharField(max_length=200)),
                ('name_address', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
