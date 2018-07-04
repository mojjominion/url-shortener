from __future__ import absolute_import, unicode_literals
from celery import task
from .models import UrlData

@task
def auto_expire():
    expired_queryset = UrlData.is_expired.all()
    expired_queryset.delete()