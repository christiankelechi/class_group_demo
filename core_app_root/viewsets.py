from rest_framework import viewsets
from core_app_root.models import ClassList
from rest_framework.permissions import AllowAny
from core_app_root.serializers import ClassListSerializer
class ClassListViewset(viewsets.ModelViewSet):
    queryset=ClassList.objects.all()
    serializer_class=ClassListSerializer
    permission_classes=[AllowAny]

