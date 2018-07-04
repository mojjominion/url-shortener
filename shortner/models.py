from django.db import models
from .utils import generate_key, create_key
from .validators import validate_url, alphanumeric
from django_hosts.resolvers import reverse
# from datetime import datetime, timedelta
import time
# Create your models here.
class UrlDataManager(models.Manager):

    def get_queryset(self):
        return super(UrlDataManager, self).get_queryset().filter(expiry_timestamp__lte=time.time())


class UrlData(models.Model):
    url                       = models.CharField(max_length=220, validators=[validate_url])
    random_key                = models.CharField(max_length=15, unique=True, blank=True, validators=[alphanumeric])
    timestamp                 = models.DateTimeField(auto_now_add=True)
    exp_in_minutes            = models.IntegerField(default=60)
    expiry_timestamp          = models.IntegerField(default=None, blank=True)
    
    objects                   = models.Manager()
    is_expired                = UrlDataManager()

    def save(self, *args, **kwargs):
        self.random_key       = create_key(self)
        self.expiry_timestamp = int(time.time() + self.exp_in_minutes*60)
        super(UrlData, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    # def get_url(url):
    #     if 'http' not in url:
    #         url="http://"+url
    #     return url

    def get_abs_url(self):
        # url = DOMAIN+'/'+url
        short_key = reverse('redirect_view', args=(self.random_key,), host='www', scheme='http')
        return short_key