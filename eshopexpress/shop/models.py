import random
import string

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def rand_slug():
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits) for _ in range(3)
    )


class Category(models.Model):
    name = models.CharField("Category", max_length=250, db_index=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='children', blank=True, null=True
    )
    slug = models.SlugField(
        'URL', max_length=250, unique=True, null=False, editable=True
    )
    created_at = models.DateTimeField('Creation date', auto_now_add=True)

    class Meta:
        unique_together = (['slug', 'parent'])
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + '-pickBetter' + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:category-list", args=[str(self.slug)])


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    title = models.CharField("Title", max_length=250)
    brand = models.CharField("Brand", max_length=250)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField('URL', max_length=250)
    price = models.DecimalField(
        "Price", max_digits=7, decimal_places=2, default=99.99
    )
    image = models.URLField("Image", blank=True)
    # image = models.ImageField("Image", upload_to='products/products/%Y/%m/%d')
    available = models.BooleanField("Availability", default=True)
    created_at = models.DateTimeField('Creation date', auto_now_add=True)
    updated_at = models.DateTimeField('Date of change', auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[str(self.slug)])


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(
            ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True
