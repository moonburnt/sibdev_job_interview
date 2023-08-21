from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from . import models
import logging

log = logging.getLogger(__name__)


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class DealsViewSet(CreateListViewSet):
    serializer_class = serializers.ClientSerializer
    # Not specified by business logic
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = models.ClientModel.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.DealSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        if self.action == "list":
            return models.ClientModel.objects.order_by("-spent_money")[:5]
        else:
            return super().get_queryset()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        resp = super().list(request, *args, **kwargs)
        gems_counter = dict()

        for entry in resp.data:
            for i in entry["gems"]:
                gems_counter[i] = gems_counter.get(i, 0) + 1

        for k, v in gems_counter.items():
            if v < 2:
                for entry in resp.data:
                    if k in entry["gems"]:
                        entry["gems"].remove(k)

        return resp
