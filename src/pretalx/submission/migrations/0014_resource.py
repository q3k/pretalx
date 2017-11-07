# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pretalx.common.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0013_auto_20171104_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(help_text='Please try to keep your upload small, preferably below 16 MB.', upload_to='', verbose_name='file')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='submission.Submission')),
            ],
            bases=(pretalx.common.mixins.LogMixin, models.Model),
        ),
    ]