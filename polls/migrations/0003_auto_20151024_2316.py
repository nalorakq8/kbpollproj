# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(to='polls.Poll', null=True),
        ),
    ]
