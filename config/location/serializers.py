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
   

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        geo_field = ("Gps","Boudary")
        fields = ("Plot_id", "Plot_name", "Plantation_id", "Planted_area", "Area_size", "Gps", "Boudary", "Listed_date", "Plot_desc")

# class TreeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Trees
#         fields = ("Tree_id", "Plot_id", "Gps", "Listed_date")

class TreeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Trees
        geo_field = "Gps"
        fields = ("Tree_id", "Plot_id", "Gps", "Listed_date")