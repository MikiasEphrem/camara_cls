# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-29 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("content", "0005_auto_20171009_0903")]

    operations = [
        migrations.AlterIndexTogether(
            name="contentnode",
            index_together=set(
                [("level", "channel_id", "kind"), ("level", "channel_id", "available")]
            ),
        )
    ]