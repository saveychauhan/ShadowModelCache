## ShadowModelCache
#### Developed by Qdagrw

ShadowModelCache is a high-performance library designed to create and manage cached copies of models, ensuring fast data retrieval and reduced load on primary data sources. It features automatic cache invalidation, various eviction policies, and supports distributed caching for scalable solutions.

### Features
- High-performance caching
- Automatic cache invalidation
- Various eviction policies
- Support for distributed caching

### How to Use

Set up the cache prefix and timeout:

```python
SMC_PREFIX = 'ShadowModelCache'
SMC_CACHE_TIMEOUT = (60 * 60 * 24)  # Cache timeout set to 24 hours
```

Define your model by extending `ShadowModelCache`:

```python
from shadowmodelcache.models import ShadowModelCache
from django.db import models

class Demo(ShadowModelCache):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.name}"
```

### In ORM

Retrieve a cached version of an object and automatically update the cache on save:

```python
Demo.objects.cget(id=1)
```

This will return a cached version of the object and update the cache automatically when the object is saved.

