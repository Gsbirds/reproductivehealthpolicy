from django.urls import path
from main.views import show_data, show_data_details

urlpatterns = [
    path("",show_data, name="show_data"),
    path("" "<int:id>/",show_data_details, name="details"),

]