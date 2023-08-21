from django.db.models import Sum
from django.db import transaction
from django.utils import timezone
import csv
import io
import logging
from datetime import datetime
from . import models

log = logging.getLogger(__name__)

FIELD_NAMES = ['customer', 'item', 'total', 'quantity', 'date']
DATETIME_FMT = "%Y-%m-%d %H:%M:%S.%f"

@transaction.atomic
def recalculate_money(clients):
    # If there was any other way to add clients, such recalculation could happen
    # via signals
    for client in clients:
        client.spent_money = client.purchases.aggregate(Sum("total"))["total__sum"]
        client.save(update_fields = ("spent_money",))

def process(csv_file):
    f = csv_file.read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(f))

    assert reader.fieldnames == FIELD_NAMES

    # Naive solution - add clients and gems right away
    # Does not scale - would need to rewrite it into bulk_create, if there
    # will be large datasets
    purchases = []

    clients = []

    for row in reader:
        client = models.ClientModel.objects.get_or_create(username=row["customer"])[0]
        gem = models.GemModel.objects.get_or_create(name=row["item"])[0]

        purchases.append(models.PurchaseModel(
            gem = gem,
            client = client,
            total = row["total"],
            quantity = row["quantity"],
            date = timezone.make_aware(
                datetime.strptime(row["date"], DATETIME_FMT)
            ),
        ))

        clients.append(client)

    models.PurchaseModel.objects.bulk_create(purchases)

    recalculate_money(clients)
