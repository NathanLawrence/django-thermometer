# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=140)),
                ('htmlCopy', models.TextField()),
                ('buttonLabel', models.CharField(max_length=50)),
                ('buttonURL', models.URLField()),
                ('fundGoal', models.IntegerField()),
                ('fundCurrent', models.IntegerField()),
            ],
        ),
    ]
