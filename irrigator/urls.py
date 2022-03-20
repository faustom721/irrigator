from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("fields", include("plants.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

admin.site.site_header = "Irrigator Admin"
admin.site.site_title = "Irrigator Admin"
admin.site.index_title = "Irrigator Admin"
