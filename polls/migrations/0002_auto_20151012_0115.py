# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(verbose_name=b'poll question', to='polls.Poll'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'last updated'),
            preserve_default=True,
        ),
    ]
