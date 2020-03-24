from django.db import models
from django.contrib.gis.db import models as geomodels


class City(models.Model):
    geom = geomodels.PointField()
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'cities'
