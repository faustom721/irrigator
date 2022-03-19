from rest_framework import viewsets

from .serializers import FieldSerializer
from .models import Field


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
