from django.db import models
from django.utils.timezone import now
from django.contrib.gis.db import models # GeoDjango Model API


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.PointField(null=True) # Spatial Field Types



class Plantation(models.Model): 
    Plantation_id = models.CharField(max_length=100, primary_key=True)
    # Organization = models.ForeignKey(Plantation_Owner_Registration, on_delete=models.DO_NOTHING)
    # Owner = models.ForeignKey(Plantation_Owner_Registration, on_delete=models.DO_NOTHING)
    Plantation_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Postcode = models.CharField(max_length=50)
    Gps = models.PointField(null=True) # Spatial Field Types
    Total_Area = models.FloatField(default=0.0,null=True)
    # Plantation_image = models.ImageField(blank=True,null=True)
    Plantation_desc = models.TextField(blank=True,null=True)
    Listed_date =models.DateTimeField(default=now)
    


class Plot(models.Model): 
    Plot_id = models.CharField(max_length=100, primary_key=True)
    Plot_name = models.CharField(max_length=100)
    Plantation_id = models.ForeignKey(Plantation, on_delete=models.DO_NOTHING,null=True)
    Planted_area = models.FloatField(default=0.0,null=True)
    Area_size = models.FloatField(default=0.0,null=True)
    Gps = models.PointField(null=True) # Spatial Field Types
    Boudary = models.PolygonField(blank=True,null=True)  #Spatial Field Types
    Listed_date =models.DateTimeField(default=now)
    Plot_desc = models.TextField(blank=True,null=True)



class Trees(models.Model): 
    Tree_id = models.CharField(max_length=100, primary_key=True)
    Listed_date =models.DateTimeField(auto_now_add=True)
    Plot_id = models.ForeignKey(Plot, on_delete=models.DO_NOTHING,null=True)
    Gps = models.PointField(null=True) # Spatial Field Types



class Trees_Health(models.Model): 
    Timestamp = models.DateTimeField(default=now, primary_key=True)
    Tree_id = models.ForeignKey(Trees, on_delete=models.DO_NOTHING,null=True)
    Mean_vari = models.FloatField(default=0.0,null=True)
    Health_class = models.CharField(max_length=100)
    # Plantation_GIS_id = models.TextField(blank=True,null=True)

