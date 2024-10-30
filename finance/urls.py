# finance/urls.py
from django.urls import path
from .views import get_stock_data

urlpatterns = [
    path('stock/<str:ticker>/', get_stock_data, name='get_stock_data'),
]