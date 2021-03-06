# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 21:40
from __future__ import unicode_literals

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('capacity', models.PositiveSmallIntegerField(default=355)),
                ('sold_out', models.BooleanField(choices=[(True, 'No more seats'), (False, 'Seats still available')], default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
