from bs4.element import ResultSet
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filter import *
from .forms import MyForm
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.db.models import Sum
from bs4 import BeautifulSoup# Create your views here.
import requests
from django.core.paginator import Paginator
def gettotal():
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    g_data = soup.find_all("div", {"class": "maincounter-number"})
    result = []
    for i in g_data:
        result.append(i.span.text)
    return result



class dienbiendich(FilterView, ListView):
    template_name = 'pages/dienbiendich.html'
    queryset = Dienbiendich.objects.all().order_by("-ngaycapnhat").order_by("-ngaycapnhat")
    models = Dienbiendich
    context_object_name = 'Dienbiendich'
    filterset_class = OrderFilter_dienbiendich
    

class covid(FilterView, ListView):
    covid_tg_total = gettotal()
    template_name = 'pages/covid.html'
    context_object_name = 'Tinhhinhcovid'
    queryset = (Tinhhinhcovid.objects.all().order_by('-ngaycapnhat', 'idcovid'))
    paginate_by = 21
    to_day = datetime.now()
    yesterday = to_day - timedelta(days=1)
    filterset_class = OrderFilter_covid
    time_vn = []
    for i in TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"):
        x = datetime.strptime(str(i.ngaycapnhat), '%d/%m/%Y')
        time_vn.append(x.strftime('%d-%m'))
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'vietnam': TinhhinhcovidVn.objects.all().order_by("ngaycapnhat")[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:],
            'thegioi': TinhhinhcovidTg.objects.all().order_by("ngaycapnhat")[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:],
            'time_vn': covid.time_vn[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:],
            'tongsoca_vn':  Tinhhinhcovid.objects.filter(ngaycapnhat = str(covid.yesterday.strftime('%Y-%m-%d')) + ' 18:00:00').aggregate(Sum('tongsoca')),
            'tuvong_vn':  Tinhhinhcovid.objects.filter(ngaycapnhat = str(covid.yesterday.strftime('%Y-%m-%d')) + ' 18:00:00').aggregate(Sum('tuvong')),
            'tongsoca_tg': self.covid_tg_total[0],
            'tuvong_tg': self.covid_tg_total[1]
        })
        return context




class vaccine(FilterView, ListView):
    template_name = 'pages/vaccine.html'
    queryset = Tinhhinhvaccine.objects.all().order_by('-ngaycapnhat', 'idvaccine')
    paginate_by = 21
    context_object_name = 'Tinhhinhvaccine'
    filterset_class = OrderFilter_vaccine
    to_day = datetime.now()
    yesterday = to_day - timedelta(days=1)
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'diadiemtiem': Diemtiemchung.objects.all().order_by("tentinhthanh"),
            'tongsomuitiem': Tinhhinhvaccine.objects.filter(ngaycapnhat = str(covid.yesterday.strftime('%Y-%m-%d')) + ' 18:00:00').aggregate(Sum('solieudatiem'))
        })
        return context 

