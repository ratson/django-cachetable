from django.conf import settings

from cachetable import models


def test_cache_models():
    assert len(settings.CACHES) == 1
    assert len(models.cache_models) == 1
