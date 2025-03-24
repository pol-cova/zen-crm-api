from django.urls import path
from .views import SaleListCreateView, SaleRetrieveUpdateDeleteView

urlpatterns = [
    path('sales/', SaleListCreateView.as_view(), name='sale-list-create'),
    path('sales/<int:pk>/', SaleRetrieveUpdateDeleteView.as_view(), name='sale-detail'),
]