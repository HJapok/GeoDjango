from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import *


@admin.register(Hotel)
class HotelAdmin(LeafletGeoAdmin):
    list_display = ("id", "name", "address", "location", "created_at", "updated_at")

@admin.register(Plantation)
class PlantationAdmin(LeafletGeoAdmin):
    list_Plantation = ("Plantation_id", "Plantation_name", "Address", "State", "Postcode", "Gps", "Total_Area", "Plantation_desc", "Listed_date")

@admin.register(Plot)
class PlotAdmin(LeafletGeoAdmin):
    list_Plot = ("Plot_id", "Plot_name", "Plantation_id", "Planted_area", "Area_size", "Gps", "Boudary", "Listed_date", "Plot_desc")

@admin.register(Trees)
class TreeTagAdmin(LeafletGeoAdmin):
    list_Tree = ("Listed_date", "Tree_id", "Plot_id", "Gps")

@admin.register(Trees_Health)
class TreeTagAdmin(LeafletGeoAdmin):
    list_Tree_Health = ("Timestamp", "Tree_id", "Mean_vari", "Health_class")