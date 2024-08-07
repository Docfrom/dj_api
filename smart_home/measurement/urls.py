from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from measurements.views import SensorViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
