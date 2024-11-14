# Create your views here.
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def index(request):
    return render(request, 'index.html')