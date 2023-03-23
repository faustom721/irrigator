from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("schedules", ScheduleViewSet)
router.register("field_plantations", PlantationFieldViewSet)

urlpatterns = [path("", include(router.urls))]
