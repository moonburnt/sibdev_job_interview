from rest_framework import serializers
from . import models
from . import parser
import logging
from django.db.models import F

log = logging.getLogger(__name__)


class ClientSerializer(serializers.ModelSerializer):
    gems = serializers.SerializerMethodField()

    class Meta:
        model = models.ClientModel
        fields = ("username", "spent_money", "gems")

    def get_gems(self, obj):
        return [
            f[0]
            for f in models.GemModel.objects.filter(purchases__client=obj)
            .values_list("name")
            .distinct()
        ]


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
