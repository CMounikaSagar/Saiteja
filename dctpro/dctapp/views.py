from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import DoctorAvailabilitySerializer
from django.db.models import Q
from django.core.cache import cache

class DoctorAvailabilityAPIView(APIView):
    def get(self, request, pk=None):
        

        doctors_count = DoctorAvailability.objects.count()
        department_count = speciality.objects.count()
        context = {
            "success": 1,
            "message": "Data fetched successfully.",
            "data": {},
            "d_count":doctors_count,
            "dept_count":department_count,
            
            
        }
        try:
            if pk :
                
                #data
                doctor = get_object_or_404(DoctorAvailability, pk=pk)
                serializer = DoctorAvailabilitySerializer(doctor)
            else:
                doctors = DoctorAvailability.objects.all()
                serializer = DoctorAvailabilitySerializer(doctors, many=True)

            context['data'] = serializer.data
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)

        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        context = {
            "success": 1,
            "message": "Data saved successfully.",
            "data": {}
        }
        try:
            serializer = DoctorAvailabilitySerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)

            doctor = serializer.save()
            context["data"] = DoctorAvailabilitySerializer(doctor).data
        except ValidationError as e:
            context["success"] = 0
            context["message"] = e.detail
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)

        print(request.data)
        print("Serializer Errors:", serializer.errors)
        return Response(context, status=status.HTTP_201_CREATED if context["success"] else status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        context = {
            "success": 1,
            "message": "Data updated successfully.",
            "data": {}
        }
        try:
            doctor = get_object_or_404(DoctorAvailability, pk=pk)
            serializer = DoctorAvailabilitySerializer(doctor, data=request.data, partial=True)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)

            doctor = serializer.save()
            context["data"] = DoctorAvailabilitySerializer(doctor).data
        except ValidationError as e:
            context["success"] = 0
            context["message"] = e.detail
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)

        return Response(context, status=status.HTTP_200_OK if context["success"] else status.HTTP_400_BAD_REQUEST)

class DoctorSearchView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            doctors = DoctorAvailability.objects.all()
            
            d_id = request.query_params.get('d_id', None)
            d_name = request.query_params.get('d_name', None)
            d_department_name = request.query_params.get('d_department_name', None)
            
            if d_id:
                doctors = doctors.filter(d_id=d_id)
            if d_name:
                doctors = doctors.filter(d_name__icontains=d_name)
            if d_department_name:
                doctors = doctors.filter(d_department__name__icontains=d_department_name)
            
            serializer = DoctorAvailabilitySerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)