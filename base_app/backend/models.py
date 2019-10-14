from django.db import models

# Create your models here.
from django.db import models


class Model1(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Model2(models.Model):

    facility_id = models.CharField(max_length=20, blank=True, null=True)
    facility_type = models.CharField(max_length=10, blank=True, null=True)
    facility_desc = models.CharField(max_length=32, blank=True, null=True)
    facility_attr0 = models.CharField(max_length=20, blank=True, null=True)
    facility_attr27 = models.CharField(max_length=60, blank=True, null=True)
    facility_attr28 = models.CharField(max_length=80, blank=True, null=True)
    basin = models.CharField(db_column='Basin', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Model2_Name'


class Model3(models.Model):
    pointid = models.CharField(db_column='PointId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pointidlong = models.CharField(db_column='PointIdLong', max_length=31, blank=True, null=True)  # Field name made lowercase.
    facilityid = models.CharField(db_column='FacilityID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    udc = models.CharField(db_column='UDC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=24, blank=True, null=True)  # Field name made lowercase.
    longdescription = models.CharField(db_column='LongDescription', max_length=80, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=16, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Model3_Name'
