from rest_framework import generics
from rest_framework import status
from .models import *

from django.contrib.gis.geos import Point,Polygon
from geopy.geocoders import Nominatim
from .serializers import *

from rest_framework.decorators import APIView
from rest_framework.response import Response
geolocator = Nominatim(user_agent="Estate")


class Plantation_list (APIView):
    def get(self, request,pk=None):
        if pk:
            example = Plantation.objects.get(pk=pk)
            serializer = PlantationSerializer(example)
            return Response(serializer.data)
        else:
            plantation_data = Plantation.objects.all()
            serializer = PlantationSerializer(plantation_data, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PlantationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        example = Plantation.objects.get(pk=pk)
        serializer = PlantationSerializer(example, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        example = Plantation.objects.get(pk=pk)
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlantationGIS(APIView):

    def get(self, request, pk=None):
        if pk:
            example = Plantation_GIS.objects.get(pk=pk)
            serializer = PlantationGISSerializer(example)
            return Response(serializer.data)
        else:
            examples = Plantation_GIS.objects.all()
            serializer = PlantationGISSerializer(examples, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PlantationGISSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        example = Plantation_GIS.objects.get(pk=pk)
        serializer = PlantationGISSerializer(example, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        example = Plantation_GIS.objects.get(pk=pk)
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Plot_list (APIView):
    def get(self, request, pk=None):
        if pk:
            example = Plot.objects.get(pk=pk)
            serializer = PlotSerializer(example)
            return Response(serializer.data)
        else:
            plot_data = Plot.objects.all()
            serializer = PlotSerializer(plot_data, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        example = Plot.objects.get(pk=pk)
        serializer = PlotSerializer(example, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        example = Plot.objects.get(pk=pk)
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Tree_CreateList (APIView):
    def get(self, request, pk=None):
        if pk:
            example = Trees.objects.get(pk=pk)
            serializer = TreeSerializer(example)
            return Response(serializer.data)
        else:
            plot_data = Trees.objects.all()
            serializer = TreeSerializer(plot_data, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        example = Trees.objects.get(pk=pk)
        serializer = TreeSerializer(example, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        example = Trees.objects.get(pk=pk)
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Tree_HealthList (APIView):
    def get(self, request, pk=None):
        if pk:
            example = Trees_Health_Info.objects.get(pk=pk)
            serializer = TreeHealthSerializer(example)
            return Response(serializer.data)
        else:
            plot_data = Trees_Health_Info.objects.all()
            serializer = TreeHealthSerializer(plot_data, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TreeHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        example = Trees_Health_Info.objects.get(pk=pk)
        serializer = TreeHealthSerializer(example, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        example = Trees_Health_Info.objects.get(pk=pk)
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

# class Tree_HealthList (APIView):
#     def get(self, request):
#         tree_data = Trees.objects.all()
#         serializer = TreeSerializer(tree_data, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         with open('/home/jagg/Documents/EBTECH/treedata1.json') as json_file:
#             # Load the JSON data from the file
#             data = json.load(json_file)

#         # Print the data
        
#         for data in data:
#             lnglat = [2.6,101.22]
#             pnt = Point(data['lng'], data['lat'])
#             tree_data = {
#                             'Plot_id':data['Plot_id'],
#                             'Gps':pnt,
#                             'Coordinate_X': data['Coor_x'],
#                             'Coordinate_X': data['Coor_y'],
#                             'Pixel_X': data['pixel_x'],
#                             'Pixel_Y': data['pixel_y'],
#                             'Mean_vari': data['Mean_Vari'],
#                             'Health_class': data['Health_class'],
#                             'Plantation_GIS_id':'1'
#                         }
#             print(tree_data)
#             serializer = TreeHealthSerializer(data=tree_data)
#             if serializer.is_valid():
#                 serializer.save()
#         return Response({'message': 'Uploaded'}, status=200)

