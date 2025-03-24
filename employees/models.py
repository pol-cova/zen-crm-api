from django.conf import settings
from django.db import models

# Create your models here.
class Employee(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employees')
    employee_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date_hired = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position} ({self.employee_number})"


    # Methods for searching employees
    @staticmethod
    def search_by_employee_number(number):
        return Employee.objects.filter(employee_number=number).first()

    @staticmethod
    def search_by_name(name):
        return Employee.objects.filter(name__icontains=name)

    @staticmethod
    def search_by_position(position):
        return Employee.objects.filter(position__icontains=position)

    # Methods for filtering employees

    @staticmethod
    def filter_by_department(department):
        return Employee.objects.filter(department__icontains=department)

    @staticmethod
    def filter_by_position(position):
        return Employee.objects.filter(position__icontains=position)

    @staticmethod
    def filter_by_date_hired(date_hired):
        return Employee.objects.filter(date_hired=date_hired)

