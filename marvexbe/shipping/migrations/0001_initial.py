# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('fk_id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('company_na', models.CharField(blank=True, db_column='COMPANY_NA', max_length=50, null=True)),
                ('alternativ', models.CharField(blank=True, db_column='ALTERNATIV', max_length=50, null=True)),
                ('managers', models.CharField(blank=True, db_column='MANAGERS', max_length=50, null=True)),
                ('manager_na', models.CharField(blank=True, db_column='MANAGER_NA', max_length=50, null=True)),
                ('date_found', models.CharField(blank=True, db_column='DATE_FOUND', max_length=15, null=True)),
                ('date_cease', models.CharField(blank=True, db_column='DATE_CEASE', max_length=15, null=True)),
                ('cessation_field', models.CharField(blank=True, db_column='CESSATION_', max_length=50, null=True)),
                ('funnel_des', models.CharField(blank=True, db_column='FUNNEL_DES', max_length=150, null=True)),
                ('flag_descr', models.CharField(blank=True, db_column='FLAG_DESCR', max_length=150, null=True)),
                ('hull_descr', models.CharField(blank=True, db_column='HULL_DESCR', max_length=149, null=True)),
                ('remarks', models.CharField(blank=True, db_column='REMARKS', max_length=250, null=True)),
                ('provenance', models.CharField(blank=True, db_column='PROVENANCE', max_length=250, null=True)),
                ('registered', models.CharField(blank=True, db_column='REGISTERED', max_length=25, null=True)),
                ('nationalit', models.CharField(blank=True, db_column='NATIONALIT', max_length=3, null=True)),
                ('jll_sighti', models.CharField(blank=True, db_column='JLL_SIGHTI', max_length=1, null=True)),
                ('registrati', models.IntegerField(blank=True, db_column='REGISTRATI', null=True)),
                ('flagpc9', models.IntegerField(blank=True, db_column='FLAGPC9', null=True)),
                ('funnelpc9', models.IntegerField(blank=True, db_column='FUNNELPC9', null=True)),
                ('flag_type', models.CharField(blank=True, db_column='FLAG_TYPE', max_length=1, null=True)),
                ('field_of_f', models.CharField(blank=True, db_column='FIELD_OF_F', max_length=2, null=True)),
                ('device_on_field', models.CharField(blank=True, db_column='DEVICE_ON_', max_length=3, null=True)),
                ('letters_on', models.CharField(blank=True, db_column='LETTERS_ON', max_length=10, null=True)),
                ('field_colo', models.CharField(blank=True, db_column='FIELD_COLO', max_length=2, null=True)),
                ('field_col2', models.CharField(blank=True, db_column='FIELD_COL2', max_length=2, null=True)),
                ('field_col3', models.CharField(blank=True, db_column='FIELD_COL3', max_length=2, null=True)),
                ('device_col', models.CharField(blank=True, db_column='DEVICE_COL', max_length=2, null=True)),
                ('device_co2', models.CharField(blank=True, db_column='DEVICE_CO2', max_length=2, null=True)),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=10, null=True)),
                ('field_dev_type', models.CharField(blank=True, db_column='_DEV_TYPE', max_length=3, null=True)),
                ('field_dev_col1', models.CharField(blank=True, db_column='_DEV_COL1', max_length=2, null=True)),
                ('field_dev_col2', models.CharField(blank=True, db_column='_DEV_COL2', max_length=2, null=True)),
                ('funn_base_field', models.CharField(blank=True, db_column='FUNN_BASE_', max_length=2, null=True)),
                ('funn_top_c', models.CharField(blank=True, db_column='FUNN_TOP_C', max_length=2, null=True)),
                ('funn_no_of', models.CharField(blank=True, db_column='FUNN_NO_OF', max_length=1, null=True)),
                ('funn_wbtb', models.IntegerField(blank=True, db_column='FUNN_WBTB', null=True)),
                ('funn_wbtb_field', models.CharField(blank=True, db_column='FUNN_WBTB_', max_length=2, null=True)),
                ('funn_wbtb2', models.CharField(blank=True, db_column='FUNN_WBTB2', max_length=2, null=True)),
                ('funn_wbtb3', models.CharField(blank=True, db_column='FUNN_WBTB3', max_length=1, null=True)),
                ('funn_panel', models.IntegerField(blank=True, db_column='FUNN_PANEL', null=True)),
                ('funn_pane2', models.CharField(blank=True, db_column='FUNN_PANE2', max_length=2, null=True)),
                ('funn_flag_field', models.IntegerField(blank=True, db_column='FUNN_FLAG_', null=True)),
                ('funn_lette', models.IntegerField(blank=True, db_column='FUNN_LETTE', null=True)),
                ('funn_lett2', models.CharField(blank=True, db_column='FUNN_LETT2', max_length=8, null=True)),
                ('funn_lett3', models.CharField(blank=True, db_column='FUNN_LETT3', max_length=2, null=True)),
                ('funn_dev1_field', models.IntegerField(blank=True, db_column='FUNN_DEV1_', null=True)),
                ('funn_dev12', models.CharField(blank=True, db_column='FUNN_DEV12', max_length=3, null=True)),
                ('funn_dev13', models.CharField(blank=True, db_column='FUNN_DEV13', max_length=2, null=True)),
                ('funn_dev14', models.CharField(blank=True, db_column='FUNN_DEV14', max_length=2, null=True)),
                ('funn_dev2_field', models.IntegerField(blank=True, db_column='FUNN_DEV2_', null=True)),
                ('funn_dev22', models.CharField(blank=True, db_column='FUNN_DEV22', max_length=3, null=True)),
                ('funn_dev23', models.CharField(blank=True, db_column='FUNN_DEV23', max_length=2, null=True)),
                ('funn_dev24', models.CharField(blank=True, db_column='FUNN_DEV24', max_length=2, null=True)),
                ('funn_bands', models.CharField(blank=True, db_column='FUNN_BANDS', max_length=2, null=True)),
                ('funn_band2', models.CharField(blank=True, db_column='FUNN_BAND2', max_length=2, null=True)),
                ('funn_lett4', models.CharField(blank=True, db_column='FUNN_LETT4', max_length=2, null=True)),
                ('funn_flag2', models.IntegerField(blank=True, db_column='FUNN_FLAG2', null=True)),
                ('funn_pane3', models.IntegerField(blank=True, db_column='FUNN_PANE3', null=True)),
                ('funn_pane4', models.CharField(blank=True, db_column='FUNN_PANE4', max_length=2, null=True)),
                ('funn_pane5', models.CharField(blank=True, db_column='FUNN_PANE5', max_length=2, null=True)),
                ('linked_pc9', models.IntegerField(blank=True, db_column='LINKED_PC9', null=True)),
                ('funn_flag3', models.CharField(blank=True, db_column='FUNN_FLAG3', max_length=2, null=True)),
                ('funn_flag4', models.CharField(blank=True, db_column='FUNN_FLAG4', max_length=2, null=True)),
                ('funn_flag5', models.CharField(blank=True, db_column='FUNN_FLAG5', max_length=2, null=True)),
                ('flag_image', models.CharField(blank=True, db_column='FLAG_IMAGE', max_length=50, null=True)),
            ],
            options={
                'db_table': 'SHIPPING',
                'managed': False,
            },
        ),
    ]
