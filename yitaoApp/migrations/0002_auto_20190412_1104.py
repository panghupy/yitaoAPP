# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-12 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yitaoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadinfo',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='是否通过审核'),
        ),
        migrations.AlterField(
            model_name='uploadinfo',
            name='phoneNumber',
            field=models.IntegerField(blank=True, max_length=12, null=True, verbose_name='手机号 (无支付宝账户可选填)'),
        ),
        migrations.AlterField(
            model_name='uploadinfo',
            name='uploader',
            field=models.CharField(max_length=32, verbose_name='邀请人 (选填)'),
        ),
    ]
