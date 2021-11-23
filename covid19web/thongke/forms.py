from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
class MyForm(forms.Form):
    my_field = DateField(widget=AdminDateWidget)