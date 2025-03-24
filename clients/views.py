from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client
from .serializers import ClientSerializer
from app.permissions import IsOwner


class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def filter_queryset(self, queryset):
        # Get filter parameters from request
        client_number = self.request.query_params.get('client_number', None)
        name = self.request.query_params.get('name', None)
        type_of_client = self.request.query_params.get('type_of_client', None)
        date_created = self.request.query_params.get('date_created', None)

        # Apply filters using your model methods
        if client_number:
            client = Client.search_by_client_number(client_number)
            if client:
                return queryset.filter(id=client.id)
            return queryset.none()

        if name:
            name_results = Client.search_by_name(name)
            return queryset.filter(id__in=name_results.values_list('id', flat=True))

        if type_of_client:
            type_results = Client.filter_by_type_of_client(type_of_client)
            return queryset.filter(id__in=type_results.values_list('id', flat=True))

        if date_created:
            date_results = Client.filter_by_date_created(date_created)
            return queryset.filter(id__in=date_results.values_list('id', flat=True))

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClientRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)