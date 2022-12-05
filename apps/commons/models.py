from django.db import models
import uuid
# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True



class BaseUUIDModel(TimeStampModel):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    class Meta:
        abstract = True


class NameDescModel(models.Model):
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)

    class Meta:
        abstract = True
