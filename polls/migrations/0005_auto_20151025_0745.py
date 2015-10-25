# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151024_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(to='polls.Poll'),
        ),
    ]
