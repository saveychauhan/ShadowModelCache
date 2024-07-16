from django.db import models

from shadowmodelcache.models import ShadowModelCache


class Demo(ShadowModelCache):

    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.name}"