from django.db import models
from django.utils.timezone import now
from django.contrib.gis.db import models # GeoDjango Model API


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
    
class Plantation_GIS(models.Model): 
    Plantation_GIS_id = models.AutoField(primary_key=True)
    Plantation_id = models.ForeignKey(Plantation, on_delete=models.DO_NOTHING,null=True)
    Raster = models.ImageField(upload_to='Raster/%Y_%m_%d/',null=True)
    DSM = models.ImageField(upload_to='DSM/%Y_%m_%d/',null=True)
    DTM = models.ImageField(upload_to='DTM/%Y_%m_%d/',null=True)
    Flow = models.ImageField(upload_to='Flow/%Y_%m_%d/',null=True)
    Vari = models.ImageField(upload_to='Vari/%Y_%m_%d/',null=True)
    IMG_bound_1 = models.PointField(null=True)
    IMG_bound_2  = models.PointField(null=True)
    Upload_Date =models.DateField(auto_now_add=True)


# class Plot(models.Model): 
#     Plot_id = models.CharField(max_length=100, primary_key=True)
#     Plot_name = models.CharField(max_length=100,null=True)
#     Plantation_id = models.ForeignKey(Plantation, on_delete=models.DO_NOTHING,null=True)
#     Planted_area = models.FloatField(default=0.0,null=True)
#     Area_size = models.FloatField(default=0.0,null=True)
#     Gps = models.PointField(null=True) # Spatial Field Types
#     Boudary = models.PolygonField(blank=True,null=True)  #Spatial Field Types
#     Listed_date =models.DateTimeField(default=now)
#     Plot_desc = models.TextField(blank=True,null=True)



# class Trees(models.Model): 
#     Tree_id = models.CharField(max_length=100, primary_key=True)
#     Listed_date =models.DateTimeField(auto_now_add=True)
#     Plot_id = models.ForeignKey(Plot, on_delete=models.DO_NOTHING,null=True)
#     Gps = models.PointField(null=True) # Spatial Field Types



# class Trees_Health_Info(models.Model): 
#     Tree_Health_id = models.AutoField(primary_key=True)
#     Timestamp = models.DateField(auto_now_add=True)
#     Plot_id = models.ForeignKey(Plot, on_delete=models.DO_NOTHING,null=True)
#     Pixel_X = models.FloatField(default=0.0,null=True)
#     Pixel_Y = models.FloatField(default=0.0,null=True)
#     Coordinate_X = models.FloatField(default=0.0,null=True)
#     Coordinate_Y = models.FloatField(default=0.0,null=True)
#     Gps = models.PointField(null=True) # Spatial Field Types
#     Mean_vari = models.FloatField(default=0.0,null=True)
#     Health_class = models.CharField(max_length=100)
#     Plantation_GIS_id = models.ForeignKey(Plantation_GIS, on_delete=models.DO_NOTHING,null=True)
#     # Upload_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

