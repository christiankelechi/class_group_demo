from rest_framework import serializers
from core_app_root.models import ClassList
class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassList
        fields=['first_name','last_name']