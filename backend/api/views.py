from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from . import models


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

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        return Response(status=status.HTTP_201_CREATED)
