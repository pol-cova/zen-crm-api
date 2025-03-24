from rest_framework import generics
from .models import Sale
from .serializers import SaleSerializer
from app.permissions import IsOwner


class SaleListCreateView(generics.ListCreateAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        # Filter sales based on the owner of the client
        return Sale.objects.filter(client__owner=self.request.user)

    def filter_queryset(self, queryset):
        # Get filter parameters from request
        ticket_number = self.request.query_params.get('ticket_number', None)
        client_id = self.request.query_params.get('client', None)
        amount = self.request.query_params.get('amount', None)
        date = self.request.query_params.get('date', None)

        # Apply filters using model methods
        if ticket_number:
            sale = Sale.search_by_ticket_number(ticket_number)
            if sale:
                return queryset.filter(id=sale.id)
            return queryset.none()

        if client_id:
            from clients.models import Client
            client = Client.objects.filter(id=client_id, owner=self.request.user).first()
            if client:
                client_results = Sale.search_by_client(client)
                return queryset.filter(id__in=client_results.values_list('id', flat=True))
            return queryset.none()

        if amount:
            amount_results = Sale.filter_by_amount(amount)
            return queryset.filter(id__in=amount_results.values_list('id', flat=True))

        if date:
            date_results = Sale.filter_by_date(date)
            return queryset.filter(id__in=date_results.values_list('id', flat=True))

        return queryset


class SaleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        return Sale.objects.filter(client__owner=self.request.user)