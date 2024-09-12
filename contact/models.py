from django.db import models
from django.utils import timezone


# id (primary key ) - automatic
# first_name (string), last_name (string), phone (string),
# email (email), description (text), created_date (date), updated_date (date),
# category (foreign key), show (boolean), owner (foreign key)
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank=True)
    # category = ...
    description = models.TextField(blank=True)
    # show = ...
    # owner = ...
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
