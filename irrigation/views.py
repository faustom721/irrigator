from calendar import weekday
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Schedule, Field
from .serializers import ScheduleSerializer, FieldSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request, *args, **kwargs):
        field = request.query_params.get("field")
        if field:
            field = get_object_or_404(Field, pk=field)
            queryset = Schedule.objects.filter(field=field)
            serialized_data = ScheduleSerializer(queryset, many=True).data
            return Response(serialized_data)
        else:
            return super().list(request, *args, **kwargs)


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
