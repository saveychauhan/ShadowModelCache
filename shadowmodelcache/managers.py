from django.db import models
from django.core.cache import cache


class CachedQuerySet(models.QuerySet):
    """ Coming soon """
    pass


class CachedManager(models.Manager):

    def get_queryset(self):
        return CachedQuerySet(self.model, using=self._db)


    def cget(self, *args, **kwargs):
        key = self.model().cache_key(kwargs[self.model().MAIN_ARG])
        cached = cache.get(key)
        if cached:
            return cached

        object = self.get_queryset().get(*args, **kwargs)
        return self.model.save_cache(key, object, self.model().CACHE_TIMEOUT)
