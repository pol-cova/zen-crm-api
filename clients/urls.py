from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDeleteView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-detail'),
]