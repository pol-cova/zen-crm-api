from django.db import models
from clients.models import Client
from employees.models import Employee

# Create your models here.
class Sale(models.Model):
    ticket_number = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sales")
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name="sales")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ticket_number} - {self.client} ({self.amount})"

    # Methods for searching sales
    @staticmethod
    def search_by_ticket_number(number):
        return Sale.objects.filter(ticket_number=number).first()

    @staticmethod
    def search_by_client(client):
        return Sale.objects.filter(client=client)

    # Methods for filtering sales
    @staticmethod
    def filter_by_amount(amount):
        return Sale.objects.filter(amount=amount)

    @staticmethod
    def filter_by_date(date):
        return Sale.objects.filter(date=date)

