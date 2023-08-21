import csv
import io
import logging
from . import models

log = logging.getLogger(__name__)

FIELD_NAMES = ['customer', 'item', 'total', 'quantity', 'date']

def process(csv_file):
    f = csv_file.read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(f))

    assert reader.fieldnames == FIELD_NAMES

    # Naive solution - add clients and gems right away
    # Does not scale - would need to rewrite it into bulk_create, if there
    # will be large datasets
    purchases = []

    for row in reader:
        client = models.ClientModel.objects.get_or_create(username=row["customer"])[0]
        gem = models.GemModel.objects.get_or_create(name=row["item"])[0]

        purchases.append(models.PurchaseModel(
            gem = gem,
            client = client,
            total = row["total"],
            quantity = row["quantity"],
            date = row["date"]
        ))
        break

    models.PurchaseModel.objects.bulk_create(purchases)
