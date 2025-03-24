from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, DateFilter
from .models import Employee
from .serializers import EmployeeSerializer
from app.permissions import IsOwner


class EmployeeFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    position = CharFilter(lookup_expr='icontains')
    department = CharFilter(lookup_expr='icontains')
    employee_number = CharFilter(lookup_expr='icontains')
    date_hired = DateFilter()

    class Meta:
        model = Employee
        fields = ['name', 'position', 'department', 'employee_number', 'date_hired']


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['name', 'position', 'department', 'employee_number']
    ordering_fields = ['name', 'date_hired', 'position', 'department', 'employee_number']
    ordering = ['employee_number']

    def get_queryset(self):
        return Employee.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Employee.objects.filter(owner=self.request.user)