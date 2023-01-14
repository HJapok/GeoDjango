from django.urls import path
from .views import *

urlpatterns = [
    path("hotels", ListCreateGenericViews.as_view()),
    path("hotels/<str:pk>",HotelUpdateRetreiveView.as_view()),
    path("plantation", Plantation_list.as_view()),
    path("plot", Plot_list.as_view()),
    path("tree", Tree_CreateList.as_view()),
]