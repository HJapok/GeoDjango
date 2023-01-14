from rest_framework import generics
from .models import Hotel

from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from .serializers import *

from rest_framework.decorators import APIView
from rest_framework.response import Response
geolocator = Nominatim(user_agent="location")


class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)


class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)

class Plantation_list (APIView):
    def get(self, request):
        plantation_data = Plantation.objects.all()
        serializer = PlantationSerializer(plantation_data, many=True)
        return Response(serializer.data)

class Plot_list (APIView):
    def get(self, request):
        plot_data = Plot.objects.all()
        serializer = PlotSerializer(plot_data, many=True)
        return Response(serializer.data)

from django.utils.timezone import now
import json
class Tree_CreateList (APIView):
    def get(self, request):
        tree_data = Trees.objects.all()
        serializer = TreeSerializer(tree_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        with open('/home/jagg/Documents/EBTECH/treedata.json') as json_file:
            # Load the JSON data from the file
            data = json.load(json_file)

        # Print the data
        
        for data in data:
            print(data)
            lnglat = [2.6,101.22]
            pnt = Point(data['lng'], data['lat'])
            tree_data = {
                            'Tree_id':data['Tree_id'],
                            'Plot_id':data['Plot_id'],
                            'Gps':pnt,
                        }
            print(tree_data)
            serializer = TreeSerializer(data=tree_data)
            if serializer.is_valid():
                serializer.save()
        return Response({'message': 'Uploaded'}, status=200)
