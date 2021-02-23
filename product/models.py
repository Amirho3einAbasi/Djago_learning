from django.db import models
from django.db.models.signals import pre_save
from product.unique_slug import unique_slug_generator


# Create your models here.
class product_object_manager(models.Manager):
    def get_exist_product(self):
        return self.get_queryset().filter(product_exist=True)

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField( default='', blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0, default=0.0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product_exist = models.BooleanField(default=True, verbose_name='موجودی')
    objects = product_object_manager()

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
