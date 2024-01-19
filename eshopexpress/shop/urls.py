from django.urls import path

from .views import category_list, products_detail_view, products_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('<slug:slug>/', products_detail_view, name='product-detail'),
    path('search/<slug:slug>/', category_list, name='category-list'),
]
