from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This is useful if you don't want to permanently erase data immediately
    deleted_at = models.DateTimeField(null=True, blank=True)

