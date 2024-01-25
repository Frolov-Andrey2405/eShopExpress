import os

import django
import requests
from django.core.exceptions import ObjectDoesNotExist
from slugify import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshopexpress.settings')
django.setup()

from shop.models import Category, Product

url = 'https://fakestoreapi.com/products'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for item in data:
        if 'category' in item:
            category_name = item['category']
            try:
                category = Category.objects.get(name=category_name)
            except ObjectDoesNotExist:
                category = Category.objects.create(name=category_name)

            product_slug = slugify(item['title'])

            Product.objects.create(
                category=category,
                title=item['title'],
                slug=product_slug,
                price=item['price'],
                description=item.get('description', ''),
                image=item.get('image', ''),
            )

    print('Successfully imported products')
else:
    print(f'Failed to fetch products. Status code: {response.status_code}')
