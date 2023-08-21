from django.db import models

class ClientModel(models.Model):
    username = models.CharField(max_length=80, unique=True)
    # virtual, calculated in serializer
    # spent_money = models.DecimalField(max_digits=8, decimal_places=2)

class GemModel(models.Model):
    name = models.CharField(max_length=80, unique=True)
    # client = models.ManyToManyField(
    #     to = ClientModel,
    #     related_name= "gems",
    # )

class PurchaseModel(models.Model):
    gem = models.ForeignKey(
        to = GemModel,
        related_name = "purchases",
        on_delete=models.CASCADE,
    )

    client = models.ForeignKey(
        to = ClientModel,
        related_name="purchases",
        on_delete=models.CASCADE,
    )

    # I assume, 'total' means "total amount of money spent on purchase"
    total = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    date = models.DateTimeField()
