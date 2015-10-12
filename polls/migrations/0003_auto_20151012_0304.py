# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151012_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(verbose_name=b'poll question', to='polls.Poll'),
            preserve_default=True,
        ),
    ]
