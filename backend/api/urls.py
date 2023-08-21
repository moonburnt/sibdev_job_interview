from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
import logging

log = logging.getLogger(__name__)


router = DefaultRouter()
router.register("deals", views.DealsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]
