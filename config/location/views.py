from rest_framework import generics
from rest_framework import status
from .models import *

from django.contrib.gis.geos import Point,Polygon
from geopy.geocoders import Nominatim
from .serializers import *

from rest_framework.decorators import APIView
from rest_framework.response import Response
geolocator = Nominatim(user_agent="location")


# class ListCreateGenericViews(generics.ListCreateAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

#     def perform_create(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)


# class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

#     def perform_update(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)

# class Plantation_list (APIView):
#     def get(self, request,pk=None):
#         if pk:
#             example = Plantation.objects.get(pk=pk)
#             serializer = PlantationSerializer(example)
#             return Response(serializer.data)
#         else:
#             plantation_data = Plantation.objects.all()
#             serializer = PlantationSerializer(plantation_data, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = PlantationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         example = Plantation.objects.get(pk=pk)
#         serializer = PlantationSerializer(example, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         example = Plantation.objects.get(pk=pk)
#         example.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class PlantationGIS(APIView):

#     def get(self, request, pk=None):
#         if pk:
#             example = Plantation_GIS.objects.get(pk=pk)
#             serializer = PlantationGISSerializer(example)
#             return Response(serializer.data)
#         else:
#             examples = Plantation_GIS.objects.all()
#             serializer = PlantationGISSerializer(examples, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = PlantationGISSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         example = Plantation_GIS.objects.get(pk=pk)
#         serializer = PlantationGISSerializer(example, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         example = Plantation_GIS.objects.get(pk=pk)
#         example.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Plot_list (APIView):
#     def get(self, request, pk=None):
#         if pk:
#             example = Plot.objects.get(pk=pk)
#             serializer = PlotSerializer(example)
#             return Response(serializer.data)
#         else:
#             plot_data = Plot.objects.all()
#             serializer = PlotSerializer(plot_data, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         plot = {
#     "Plot_id": "plot_1",
#     "Plot_name": "plot one",
#     "Plantation_id": "plantation_1",
#     "Planted_area": 800.0,
#     "Area_size": 1000.0,
#     "Gps": Point(102.21699588649794, 5.415244376447327),
#     "Boudary": Polygon( ((
#                     102.2165935006721, 
#                     5.415570145398239
#                 ), 
#                 (
#                     102.21675445500246, 
#                     5.415725019100209
#                 ), 
#                 (   
#                     102.21701198193097, 
#                     5.415751721458614
#                 ), 
#                 (   
#                     102.21713538025091, 
#                     5.415564804925056
#                 ), 
#                 (   
#                     102.21719976198304, 
#                     5.415244376447327
#                 ), 
#                 (   102.21725877857085, 
#                     5.4149079263628686
#                 ), 
#                 (   102.21707099851878, 
#                     5.414806457253019
#                 ), 
#                 (
#                     102.21687785332237, 
#                     5.414934628757367
#                 ), 
#                 (   102.21669543841463, 
#                     5.415329824058001
#                 )) ),
#     "Plot_desc": "this is plot one"
# }

#         serializer = PlotSerializer(data=plot)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         example = Plot.objects.get(pk=pk)
#         serializer = PlotSerializer(example, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         example = Plot.objects.get(pk=pk)
#         example.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Tree_CreateList (APIView):
#     def get(self, request, pk=None):
#         if pk:
#             example = Trees.objects.get(pk=pk)
#             serializer = TreeSerializer(example)
#             return Response(serializer.data)
#         else:
#             plot_data = Trees.objects.all()
#             serializer = TreeSerializer(plot_data, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = TreeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         example = Plot.objects.get(pk=pk)
#         serializer = TreeSerializer(example, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         example = Trees.objects.get(pk=pk)
#         example.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from django.utils.timezone import now
# import json
# class Tree_CreateList (APIView):
#     def get(self, request):
#         tree_data = Trees.objects.all()
#         serializer = TreeSerializer(tree_data, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         with open('/home/jagg/Documents/EBTECH/treedata.json') as json_file:
#             # Load the JSON data from the file
#             data = json.load(json_file)

#         # Print the data
        
#         for data in data:
#             print(data)
#             lnglat = [2.6,101.22]
#             pnt = Point(data['lng'], data['lat'])
#             tree_data = {
#                             'Tree_id':data['Tree_id'],
#                             'Plot_id':data['Plot_id'],
#                             'Gps':pnt,
#                         }
#             print(tree_data)
#             serializer = TreeSerializer(data=tree_data)
#             if serializer.is_valid():
#                 serializer.save()
#         return Response({'message': 'Uploaded'}, status=200)
