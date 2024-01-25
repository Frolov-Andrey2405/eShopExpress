# Console commands to use

Activate venv:

```bash
.\venv\Scripts\activate
```

Django makemigrations, migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

Django runserver:

```bash
cd .\eshopexpress\
python.exe .\manage.py runserver
```

Freeze:

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Redis-server:

```bash
cd .\eshopexpress\redis-x64-3.0.504
.\redis-server.exe
```

Celery worker:

```bash
celery -A eshopexpress worker -l info
```

Celery beat:

```bash
celery -A eshopexpress beat -l info
```

Celery flower:

```bash
celery -A eshopexpress flower
```

Stripe webhook:

```bash
cd .\eshopexpress\stripe
stripe.exe
stripe login
stripe listen --forward-to localhost:8000/payment/webhook-stripe/
```
