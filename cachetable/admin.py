import base64
import pickle

from django.db import models
from django.forms import TextInput
from django.utils.encoding import force_bytes

from django.contrib import admin
from django.contrib.humanize.templatetags import humanize

from .models import cache_models


class ReadOnlyDateTimeInput(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        return value


class CacheTableAdmin(admin.ModelAdmin):
    list_display = ('cache_key', 'expires_at')
    search_fields = ('cache_key',)
    readonly_fields = ('cache_key', 'value', 'decoded_value')
    ordering = ('-expires', 'cache_key')

    formfield_overrides = {
        models.DateTimeField: {'widget': ReadOnlyDateTimeInput()},
    }

    def expires_at(self, obj):
        return humanize.naturaltime(obj.expires)
    expires_at.admin_order_field = 'expires'

    def decoded_value(self, obj):
        return pickle.loads(base64.b64decode(force_bytes(obj.value)))

    def has_add_permission(self, request):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super().changeform_view(
            request, object_id, extra_context=extra_context)


for x in cache_models:
    admin.site.register(x, CacheTableAdmin)
