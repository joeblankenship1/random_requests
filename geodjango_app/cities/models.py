from django.db import models
from django.contrib.gis.db import models as geomodels


class Cities500(models.Model):
    geom = models.PointField(blank=True, null=True)
    field_1 = models.IntegerField(blank=True, null=True)
    field_2 = models.CharField(max_length=-1, blank=True, null=True)
    field_3 = models.CharField(max_length=-1, blank=True, null=True)
    field_4 = models.CharField(max_length=-1, blank=True, null=True)
    field_5 = models.FloatField(blank=True, null=True)
    field_6 = models.FloatField(blank=True, null=True)
    field_7 = models.CharField(max_length=-1, blank=True, null=True)
    field_8 = models.CharField(max_length=-1, blank=True, null=True)
    field_9 = models.CharField(max_length=-1, blank=True, null=True)
    field_10 = models.CharField(max_length=-1, blank=True, null=True)
    field_11 = models.CharField(max_length=-1, blank=True, null=True)
    field_12 = models.CharField(max_length=-1, blank=True, null=True)
    field_13 = models.CharField(max_length=-1, blank=True, null=True)
    field_14 = models.CharField(max_length=-1, blank=True, null=True)
    field_15 = models.IntegerField(blank=True, null=True)
    field_16 = models.IntegerField(blank=True, null=True)
    field_17 = models.IntegerField(blank=True, null=True)
    field_18 = models.CharField(max_length=-1, blank=True, null=True)
    field_19 = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cities500'
