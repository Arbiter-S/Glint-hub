from django.db import models
import datetime


# Create your models here.


def image_path(instance, filename):
    # MEDIA_ROOT / user_ < id > / < filename >
    uploaded_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return f"products/{instance.category}/{instance.name + '_' + uploaded_date}.jpeg"


class Product(models.Model):
    categories = [
        ("neck", "Necklace"),
        ("brace", "Bracelet"),
        ("watch", "Watch"),
        ("ear", "Earring"),
    ]

    name = models.CharField(max_length=55)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=25)
    in_stock = models.SmallIntegerField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=categories)
    purity = models.SmallIntegerField()
    picture = models.ImageField(upload_to=image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
