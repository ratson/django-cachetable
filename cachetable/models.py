from django.conf import settings
from django.core.cache import caches
from django.core.cache.backends.db import BaseDatabaseCache
from django.db import models


class CacheTable(models.Model):
    cache_key = models.CharField(max_length=255, primary_key=True,
                                 editable=False)
    value = models.TextField(editable=False)
    expires = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def __str__(self):
        return self.cache_key


cache_models = []

for k, v in settings.CACHES.items():
    cache = caches[k]
    if not isinstance(cache, BaseDatabaseCache):
        continue

    class CacheTableMeta:
        db_table = v['LOCATION']
        managed = False

    cache_models.append(type('{}Cache'.format(k.title()), (CacheTable,), {
        'Meta': CacheTableMeta,
        '__module__': CacheTable.__module__,
    }))
