#python imports.
import uuid

#django imports.
from django.db import models

#project level imports.
from libs.models import TimeStampedModel


class AdressLtude(TimeStampedModel):
    """
    AddressLtude model stores the longitude and latitude data of corresonding address
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.TextField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)

    
