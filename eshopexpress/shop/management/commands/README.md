# Fake Product Generator

Two scripts for generating fake product data for a Django project are presented. Choose `fakeproducts.py` or `fakestoreapi.py` depending on your preference.

## Usage

### 1. Fake Product Generator (`fakeproducts.py`)

Generates fake product data using the Faker library:

```bash
python manage.py fakeproducts
```

By default, this script generates 30 fake products. Adjust the number as needed.

### 2. Fake Store API Importer (``fakestoreapi.py``)

Imports product data from the Fake Store API:

```bash
python fakestoreapi.py
```

This script retrieves data from [Fake Store API](https://fakestoreapi.com/products) and populates your database.

Choose a script that fits your requirements and run it to populate your Django project's database with information about fake goods.