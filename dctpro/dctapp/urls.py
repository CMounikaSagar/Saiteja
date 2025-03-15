from django.urls import path
from django.http import HttpResponse
from .views import *

def home(request):
    return HttpResponse("Django is successfully deployed!")

urlpatterns = [
    # path('doctors-ui/', doctor_list_view, name='doctor-list-ui'),
    # path('speciality/', SpecialityAPIView.as_view(), name='speciality'),
    # path('recent-searches/', RecentSearchesAPIView.as_view(), name='recent-searches'),
    # path('doctors/', DoctorAPIView.as_view(), name='doctor-list'),
    path('',home),
    path('doctors/', DoctorAvailabilityAPIView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorAvailabilityAPIView.as_view(), name='doctor-detail'),
    path('doctor/',DoctorSearchView.as_view(),name='doctor')
]
