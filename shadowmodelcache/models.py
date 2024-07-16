from django.core.cache import cache
from django.db import models
from django.conf import settings
from shadowmodelcache.managers import CachedManager
from shadowmodelcache.utils import save_model_cache, delete_model_cache


class ShadowModelCache(models.Model):


    MAIN_ARG = 'id'
    CACHE_PREFIX = None
    CACHE_TIMEOUT = settings.SMC_CACHE_TIMEOUT
    objects = CachedManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def cache_key(self, value):
        return self.get_cache_key(value)

    def get_cache_key(self, value):
        if self.CACHE_PREFIX:
            return f"{self.CACHE_PREFIX}:{self.MAIN_ARG}:{value}"

        app_label = self._meta.app_label
        verbose_name = self._meta.verbose_name
        return f"{app_label}:{verbose_name}:{self.MAIN_ARG}:{value}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        key = self.cache_key(getattr(self, self.MAIN_ARG))
        self.save_cache(key, self, self.CACHE_TIMEOUT)

    @staticmethod
    def save_cache(key, obj, timeout):
        return save_model_cache(key, obj=obj, cache_timeout=timeout)


    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_model_cache(self.cache_key(kwargs[self.MAIN_ARG]))


    class Meta:
        abstract = True