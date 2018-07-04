from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='www'),
    # host(r'(?!www).*', 'path.to.custom_urls', name='wildcard'),
)
