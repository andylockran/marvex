# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_code', models.CharField(blank=True, help_text='The original code used in the Approach database.', max_length=10, null=True)),
                ('iso_code3', models.CharField(blank=True, help_text='The official 3 digit ISO code.', max_length=3, null=True)),
                ('iso_code2', models.CharField(blank=True, help_text='The official 2 digit ISO code.', max_length=2, null=True)),
                ('long_name', models.CharField(blank=True, help_text='The official name.', max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='shipping',
            options={'managed': False, 'ordering': ['fk_id']},
        ),
    ]
