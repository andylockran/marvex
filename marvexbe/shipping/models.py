# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Country (models.Model):
    original_code = models.CharField(max_length=10, blank=True, null=True, help_text="The original code used in the Approach database.")
    iso_code3 = models.CharField(max_length=3, blank=True, null=True, help_text="The official 3 digit ISO code.")
    iso_code2 = models.CharField(max_length=2, blank=True, null=True, help_text="The official 2 digit ISO code.")
    long_name = models.CharField(max_length=50, blank=True, null=True, help_text="The official name.")

class Shipping(models.Model):
    fk_id      = models.IntegerField(db_column='id', primary_key=True, help_text="The unique identifier for the record, legacy from the original approach database.")
    company_name = models.CharField(db_column='COMPANY_NA', max_length=50, blank=True, null=True, help_text="The company's primary name.")  # Field name made lowercase.
    alternative_name = models.CharField(db_column='ALTERNATIV', max_length=50, blank=True, null=True, help_text="Any alternative names for the company.")  # Field name made lowercase.
    managers = models.CharField(db_column='MANAGERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manager_names = models.CharField(db_column='MANAGER_NA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_founded = models.CharField(db_column='DATE_FOUND', max_length=15, blank=True, null=True, help_text="The year the company was founded (not always a single year).")  # Field name made lowercase.
    date_ceased = models.CharField(db_column='DATE_CEASE', max_length=15, blank=True, null=True, help_text="The year the company ceased")  # Field name made lowercase.
    cessation_field = models.CharField(db_column='CESSATION_', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funnel_description = models.CharField(db_column='FUNNEL_DES', max_length=150, blank=True, null=True)  # Field name made lowercase.
    flag_description = models.CharField(db_column='FLAG_DESCR', max_length=150, blank=True, null=True)  # Field name made lowercase.
    hull_description = models.CharField(db_column='HULL_DESCR', max_length=149, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    provenance = models.CharField(db_column='PROVENANCE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    registered = models.CharField(db_column='REGISTERED', max_length=25, blank=True, null=True, help_text="The city of registration.")  # Field name made lowercase.
    nationality = models.CharField(db_column='NATIONALIT', max_length=3, blank=True, null=True, help_text="The registered nationality of the ship.")  # Field name made lowercase.
    country = models.ForeignKey(Country, blank=True, null=True)
    jll_sighted = models.CharField(db_column='JLL_SIGHTI', max_length=1, blank=True, null=True, help_text="Y/N field for whether this was spotted by Louis Loughran.")  # Field name made lowercase.
    registration = models.IntegerField(db_column='REGISTRATI', blank=True, null=True)  # Field name made lowercase.
    flagpc9 = models.IntegerField(db_column='FLAGPC9', blank=True, null=True)  # Field name made lowercase.
    funnelpc9 = models.IntegerField(db_column='FUNNELPC9', blank=True, null=True)  # Field name made lowercase.
    flag_type = models.CharField(db_column='FLAG_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    field_of_f = models.CharField(db_column='FIELD_OF_F', max_length=2, blank=True, null=True)  # Field name made lowercase.
    device_on_field = models.CharField(db_column='DEVICE_ON_', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    letters_on = models.CharField(db_column='LETTERS_ON', max_length=10, blank=True, null=True)  # Field name made lowercase.
    field_colo = models.CharField(db_column='FIELD_COLO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field_col2 = models.CharField(db_column='FIELD_COL2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field_col3 = models.CharField(db_column='FIELD_COL3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    device_col = models.CharField(db_column='DEVICE_COL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    device_co2 = models.CharField(db_column='DEVICE_CO2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    field_dev_type = models.CharField(db_column='_DEV_TYPE', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dev_col1 = models.CharField(db_column='_DEV_COL1', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dev_col2 = models.CharField(db_column='_DEV_COL2', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    funn_base_field = models.CharField(db_column='FUNN_BASE_', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funn_top_c = models.CharField(db_column='FUNN_TOP_C', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_no_of = models.CharField(db_column='FUNN_NO_OF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    funn_wbtb = models.IntegerField(db_column='FUNN_WBTB', blank=True, null=True)  # Field name made lowercase.
    funn_wbtb_field = models.CharField(db_column='FUNN_WBTB_', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funn_wbtb2 = models.CharField(db_column='FUNN_WBTB2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_wbtb3 = models.CharField(db_column='FUNN_WBTB3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    funn_panel = models.IntegerField(db_column='FUNN_PANEL', blank=True, null=True)  # Field name made lowercase.
    funn_pane2 = models.CharField(db_column='FUNN_PANE2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_flag_field = models.IntegerField(db_column='FUNN_FLAG_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funn_lette = models.IntegerField(db_column='FUNN_LETTE', blank=True, null=True)  # Field name made lowercase.
    funn_lett2 = models.CharField(db_column='FUNN_LETT2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    funn_lett3 = models.CharField(db_column='FUNN_LETT3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_dev1_field = models.IntegerField(db_column='FUNN_DEV1_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funn_dev12 = models.CharField(db_column='FUNN_DEV12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    funn_dev13 = models.CharField(db_column='FUNN_DEV13', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_dev14 = models.CharField(db_column='FUNN_DEV14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_dev2_field = models.IntegerField(db_column='FUNN_DEV2_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    funn_dev22 = models.CharField(db_column='FUNN_DEV22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    funn_dev23 = models.CharField(db_column='FUNN_DEV23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_dev24 = models.CharField(db_column='FUNN_DEV24', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_bands = models.CharField(db_column='FUNN_BANDS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_band2 = models.CharField(db_column='FUNN_BAND2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_lett4 = models.CharField(db_column='FUNN_LETT4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_flag2 = models.IntegerField(db_column='FUNN_FLAG2', blank=True, null=True)  # Field name made lowercase.
    funn_pane3 = models.IntegerField(db_column='FUNN_PANE3', blank=True, null=True)  # Field name made lowercase.
    funn_pane4 = models.CharField(db_column='FUNN_PANE4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_pane5 = models.CharField(db_column='FUNN_PANE5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    linked_pc9 = models.IntegerField(db_column='LINKED_PC9', blank=True, null=True)  # Field name made lowercase.
    funn_flag3 = models.CharField(db_column='FUNN_FLAG3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_flag4 = models.CharField(db_column='FUNN_FLAG4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funn_flag5 = models.CharField(db_column='FUNN_FLAG5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    flag_image = models.CharField(db_column='FLAG_IMAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        managed = True
        db_table = 'SHIPPING'
        ordering = ['fk_id']        
    
    def __unicode__(self):
            return str(self.company_name)
