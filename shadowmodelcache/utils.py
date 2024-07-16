from django.core.cache import cache

def save_model_cache(key, obj, cache_timeout):
    cache.set(key, obj, timeout=cache_timeout)
    return obj

def delete_model_cache(key):
    cache.delete(key)
    return key



