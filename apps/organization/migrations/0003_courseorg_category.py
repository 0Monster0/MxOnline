# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180327_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pejg', '\u57f9\u8bad\u673a\u6784'), ('gx', '\u9ad8\u6821 '), ('gr', '\u4e2a\u4eba')], default='pxjg', max_length=20),
        ),
    ]