# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170402_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='english_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='polish_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
