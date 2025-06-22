from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings
import os

# Create your models here.

def create_qr_code(data):
    qr = qrcode.make(data)
    blob = BytesIO()
    qr.save(blob, 'PNG')
    return File(blob, name='qr.png')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    def save(self, *args, **kwargs):
        # Define the data to encode
        qr_data = f"http://127.0.0.1:8000/api/scan/{self.employee_id}/"
        self.qr_code = create_qr_code(qr_data)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name