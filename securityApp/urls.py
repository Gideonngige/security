from django.urls import path
from . import views

urlpatterns = [
    path('security/', views.security, name='security'),
    path('employee_qr/<str:employee_id>/', views.employee_qr, name='employee_qr'),
    path('qr_code/', views.qr_code, name='qr_code'),
]