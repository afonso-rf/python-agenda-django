from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key ) - automatic
# first_name (string), last_name (string), phone (string),
# email (email), description (text), created_date (date),
# updated_date (date), category (foreign key), show (boolean),
# owner (foreign key), picture (image)


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        default=timezone.now,
    )
    updated_date = models.DateTimeField(
        default=timezone.now,
    )
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
