from rest_framework import serializers
from . import models
from . import parser
import logging

log = logging.getLogger(__name__)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientModel
        fields = "__all__"


class GemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GemModel
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseModel
        fields = "__all__"


class DealSerializer(serializers.Serializer):
    deals = serializers.FileField(required=True)

    def save(self):
        try:
            parser.process(self.validated_data["deals"])
        except Exception as e:
            raise serializers.ValidationError(e)
