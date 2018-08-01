# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Model based on an existing DB via inpectdb

class Trafficnow(models.Model):
    date = models.DateTimeField(blank=True, null=False, primary_key=True)
    bin = models.TextField(blank=True, null=True)
    day = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    km = models.TextField(blank=True, null=True)
    location_1 = models.TextField(blank=True, null=True)
    location_2 = models.TextField(blank=True, null=True)
    road = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trafficnow'
