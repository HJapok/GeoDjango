from location.models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel

        fields = ("id", "name", "address", "location")

        extra_kwargs = {"location": {"read_only": True}}

class PlantationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantation
        fields = ("Plantation_id", "Plantation_name", "Address", "State", "Postcode", "Gps", "Total_Area", "Plantation_desc", "Listed_date")

class PlantationGISSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantation_GIS
        fields = ("Plantation_GIS_id", "Plantation_id", "Raster", "DSM", "DTM", "Flow", "Vari", "IMG_bound_1", "IMG_bound_2", "Upload_Date")
   

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ("Plot_id", "Plot_name", "Plantation_id", "Planted_area", "Area_size", "Gps", "Boudary", "Listed_date", "Plot_desc")

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trees
        fields = ("Tree_id", "Plot_id", "Gps", "Listed_date")