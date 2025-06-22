from django import forms

class QRRequestForm(forms.Form):
    employee_id = forms.CharField(label="Enter your Employee ID", max_length=20)
