from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    employees = Employee.objects.all()

    if request.POST:
        name = request.POST.get('employee_name')
        Employee.objects.create(name=name)
        employees = Employee.objects.all()
        
    
    return render(request, 'employee.html', {
        'employees': employees,
    })
