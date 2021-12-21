from django.db import models
from django.conf import settings

from ..core.models import TimestampedModel

# Create your models here.


class Payment(TimestampedModel):
    tx_ref = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_recurring = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user
