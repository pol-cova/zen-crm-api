from django.conf import settings
from django.db import models

# Create your models here.
class Client(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients')
    client_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    type_of_client = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.type_of_client} ({self.client_number})"

    # Methods for searching clients
    @staticmethod
    def search_by_client_number(number):
        return Client.objects.filter(client_number=number).first()

    @staticmethod
    def search_by_name(name):
        return Client.objects.filter(name__icontains=name)

    # Methods for filtering clients
    @staticmethod
    def filter_by_type_of_client(type_of_client):
        return Client.objects.filter(type_of_client__icontains=type_of_client)

    @staticmethod
    def filter_by_date_created(date_created):
        return Client.objects.filter(date_created=date_created)

