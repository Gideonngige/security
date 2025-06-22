from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Employee
from .forms import QRRequestForm

# Create your views here.
def security(request):
    return HttpResponse("Hello world!")

def employee_qr(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    return render(request, 'qr_display.html', {'employee': employee})


def qr_code(request):
    form = QRRequestForm()
    employee = None
    error = None

    if request.method == 'POST':
        form = QRRequestForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                error = "Invalid Employee ID. Please try again."

    return render(request, 'qr_form.html', {
        'form': form,
        'employee': employee,
        'error': error
    })

def qr_scan(request, code):
    try:
        employee = Employee.objects.get(employee_id=code)

        return JsonResponse({
            'status': 'success',
            'message': 'Access Granted',
            'employee_name': employee.name
        })

    except Employee.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid QR Code'
        }, status=404)