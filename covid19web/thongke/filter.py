import django_filters
import datetime
from datetime import datetime, timedelta
from django import forms
from .models import *
from django_filters import rest_framework as filters

def get_date_vaccine():
    base = datetime.now() - timedelta(days=1)
    date_set = set([base - timedelta(days=x) for x in range(5)])
    booking_dates = set(Tinhhinhvaccine.objects.all().values_list('ngaycapnhat_id', flat=True))
    valid_dates = date_set
    date_choices = sorted([(valid_date.strftime('%Y-%m-%d')+ ' 18:00:00', valid_date.strftime('%d-%m-%Y')) for valid_date in valid_dates], 
                      key=lambda x: x[0])
    return date_choices

def get_tinhthanh_vaccine():
    tinhthanh_choices = []
    tinhthanh = set(Tinhhinhvaccine.objects.all().values_list('tentinhthanh', flat=True))
    tinhthanh2 = tinhthanh
    for tinh in tinhthanh2:
        tinhthanh_choices.append((tinh, tinh))
    return sorted(tinhthanh_choices)
    
class OrderFilter_vaccine(django_filters.FilterSet):
    tentinhthanh = django_filters.ChoiceFilter(label='Tỉnh/TP', choices=get_tinhthanh_vaccine())
    ngaycapnhat = django_filters.ChoiceFilter(label = "Ngày:", choices=get_date_vaccine())
    def __init__(self, *args, **kwargs):
        super(OrderFilter_vaccine, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Tinhhinhvaccine
        fields = ['ngaycapnhat', 'tentinhthanh']

def get_date_covid():
    base = datetime.now() - timedelta(days=1)
    date_set = set([base - timedelta(days=x) for x in range(5)])
    booking_dates = set(Tinhhinhcovid.objects.all().values_list('ngaycapnhat_id', flat=True))
    valid_dates = date_set
    date_choices = sorted([(valid_date.strftime('%Y-%m-%d')+ ' 18:00:00', valid_date.strftime('%d-%m-%Y')) for valid_date in valid_dates], 
                      key=lambda x: x[0])
    return date_choices

def get_tinhthanh_covid():
    tinhthanh_choices = []
    tinhthanh = set(Tinhhinhcovid.objects.all().values_list('tentinhthanh', flat=True))
    tinhthanh2 = tinhthanh
    for tinh in tinhthanh2:
        tinhthanh_choices.append((tinh, tinh))
    return sorted(tinhthanh_choices)

class OrderFilter_covid(django_filters.FilterSet):
    tentinhthanh = django_filters.ChoiceFilter(label='Tỉnh/TP', choices=get_tinhthanh_covid())
    ngaycapnhat = django_filters.ChoiceFilter(label = "Ngày:", choices=get_date_covid   ())
    def __init__(self, *args, **kwargs):
        super(OrderFilter_covid, self).__init__(*args, **kwargs)
    class Meta:
        model = Tinhhinhvaccine
        fields = ['ngaycapnhat', 'tentinhthanh']


def get_date_dienbiendich():
    base = datetime.now() - timedelta(days=1)
    date_set = set([base - timedelta(days=x) for x in range(5)])
    booking_dates = set(Dienbiendich.objects.all().values_list('ngaycapnhat_id', flat=True))
    valid_dates = date_set
    date_choices = sorted([(valid_date.strftime('%Y-%m-%d')+ ' 18:00:00', valid_date.strftime('%d-%m-%Y')) for valid_date in valid_dates], 
                      key=lambda x: x[0])
    return date_choices

class OrderFilter_dienbiendich(django_filters.FilterSet):
    ngaycapnhat = django_filters.ChoiceFilter(label = "Ngày:", choices=get_date_dienbiendich())
    def __init__(self, *args, **kwargs):
        super(OrderFilter_dienbiendich, self).__init__(*args, **kwargs)

    class Meta:
        model = Tinhhinhvaccine
        fields = ['ngaycapnhat']