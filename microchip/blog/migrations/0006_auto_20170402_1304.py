# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170402_1132'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('polish_link', 'english_link')]),
        ),
    ]