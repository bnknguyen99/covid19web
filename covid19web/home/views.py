from django.shortcuts import render
from django.http import HttpResponse
from thongke.models import Tinhhinhcovid
from thongke.models import TinhhinhcovidVn
from thongke.models import Dienbiendich
from tintuc.models import Baiviet
from .forms import RegistrationForm 
from django.http import HttpResponseRedirect
import datetime
from django_filters.views import FilterView
from django.views.generic import ListView, DetailView



class home(ListView):
    template_name = 'pages/home.html'
    context_object_name = 'Tinhhinhcovid'
    queryset = Tinhhinhcovid.objects.all().order_by("-ngaycapnhat")
    time = []
    to_day = datetime.datetime.now()
    yesterday = to_day - datetime.timedelta(days=1) 
    for i in TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"):
        x = datetime.datetime.strptime(str(i.ngaycapnhat), '%d/%m/%Y')
        time.append(x.strftime('%d-%m'))
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'covid' : Tinhhinhcovid.objects.raw("Select * from web.tinhhinhcovid where ngaycapnhat = '%s'" % (str(home.yesterday.strftime('%Y-%m-%d')) + ' 18:00:00')),
            'dienbien': Dienbiendich.objects.latest("ngaycapnhat"),
            'tintuc': Baiviet.objects.all().order_by("-ngaydangbaiviet")[:6],
            'vietnam': TinhhinhcovidVn.objects.all().order_by("ngaycapnhat")[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:],
            'time_vn': home.time[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:]
        })
        return context


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.get_full_path())
    return render(request, 'pages/register.html', {'form': form})

