from django.urls import path,re_path
from .views import *

urlpatterns = [
    path("plantation/", Plantation_list.as_view()),
    path("plantation/<str:pk>/", Plantation_list.as_view()),
    path("plot/", Plot_list.as_view()),
    path("plot/<str:pk>/", Plot_list.as_view()),
    path("tree/", Tree_CreateList.as_view()),
    path("tree/<str:pk>/", Tree_CreateList.as_view()),
    path("plantationGIS/", PlantationGIS.as_view(), name='plantationGIS-list'),
    path("plantationGIS/<int:pk>/", PlantationGIS.as_view(), name='plantationGIS-detail'),
    path("treehealth/", Tree_HealthList.as_view()),
    path("treehealth/<int:pk>/", Tree_CreateList.as_view()),
]