# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_auto_20180326_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='flag_descr',
            new_name='flag_description',
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='funnel_des',
            new_name='funnel_description',
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='hull_descr',
            new_name='hull_description',
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='manager_na',
            new_name='manager_names',
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='registrati',
            new_name='registration',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='alternativ',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='company_na',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='date_cease',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='date_found',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='jll_sighti',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='nationalit',
        ),
        migrations.AddField(
            model_name='shipping',
            name='alternative_name',
            field=models.CharField(blank=True, db_column='ALTERNATIV', help_text='Any alternative names for the company.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='company_name',
            field=models.CharField(blank=True, db_column='COMPANY_NA', help_text="The company's primary name.", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.Country'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='date_ceased',
            field=models.CharField(blank=True, db_column='DATE_CEASE', help_text='The year the company ceased', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='date_founded',
            field=models.CharField(blank=True, db_column='DATE_FOUND', help_text='The year the company was founded (not always a single year).', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='jll_sighted',
            field=models.CharField(blank=True, db_column='JLL_SIGHTI', help_text='Y/N field for whether this was spotted by Louis Loughran.', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='nationality',
            field=models.CharField(blank=True, db_column='NATIONALIT', help_text='The registered nationality of the ship.', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='fk_id',
            field=models.IntegerField(db_column='id', help_text='The unique identifier for the record, legacy from the original approach database.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='registered',
            field=models.CharField(blank=True, db_column='REGISTERED', help_text='The city of registration.', max_length=25, null=True),
        ),
    ]