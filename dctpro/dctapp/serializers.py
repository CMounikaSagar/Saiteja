from rest_framework import serializers
from .models import *
from .validators import validate_email

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    d_department_name = serializers.CharField(source="d_department.name", read_only=True)
    d_email = serializers.EmailField(
        max_length=255,
        validators=[validate_email],  # ✅ Apply the validator
        error_messages={
            "invalid": ("Enter a valid email address ending with '.com'."),
            "max_length": ("Email cannot exceed 255 characters."),
            "blank": ("Email cannot be empty."),
        }
    )

    class Meta:
        model = DoctorAvailability
        fields = "__all__"

    
    
   
# class NurseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Nurse
#         fields = '_all_'
    
#     def validate_email(self, value):
#        validate_email(value)
#        return value

# class PharmacySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pharmacy
#         fields = '_all_'
        
#     def validate_email(self, value):
#        validate_email(value)
#        return value

# class OtherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Other
#         fields = '_all_'
        
#     def validate_email(self, value):
#        validate_email(value)
#        return value
        
# class SpecialtySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = speciality
#         fields = '_all_'
        
#     def validate_email(self, value):
#        validate_email(value)
#        return value
   
    
   