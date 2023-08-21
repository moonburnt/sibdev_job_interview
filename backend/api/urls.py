from django.urls import path, include
from api import views
import logging

log = logging.getLogger(__name__)

urlpatterns = [
    path("", views.DealsViewSet.as_view({"get": "list", "post": "create"})),
]
