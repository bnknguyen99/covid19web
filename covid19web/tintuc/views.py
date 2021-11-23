from django.db import models
from django.http import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Baiviet, Binhluan, Chudebaiviet
from thongke.models import TinhhinhcovidVn
from .forms import CommentForm
import datetime
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseBadRequest

class hienthibaiviet(ListView):
    template_name = 'pages/tintuc.html'
    context_object_name = 'Baiviet'
    paginate_by = 4
    queryset = Baiviet.objects.all().order_by("-ngaydangbaiviet")
    time = []
    for i in TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"):
        x = datetime.datetime.strptime(str(i.ngaycapnhat), '%d/%m/%Y')
        time.append(x.strftime('%d-%m'))
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'category': Chudebaiviet.objects.all(),
            'vietnam': TinhhinhcovidVn.objects.all().order_by("ngaycapnhat")[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:],
            'time': hienthibaiviet.time[len(TinhhinhcovidVn.objects.all().order_by("ngaycapnhat"))-7:]
        })
        return context

class noidungbaiviet(DetailView):
    context_object_name = 'Baiviet'
    model = Baiviet
    template_name = 'pages/baiviet.html'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({
            'category': Chudebaiviet.objects.all()
        })
        return context    


def post_comments_controller(request, pk):
    from .forms import CommentForm
    comment_form = CommentForm(request.POST or None)
    topic = Baiviet.objects.get(idbaiviet = pk)
    binhluan = Binhluan.objects.filter(baiviet = topic).order_by('-ngaydangbinhluan')
    if comment_form.is_valid():
        comment_obj = comment_form.save(commit=False)
        comment_obj.taikhoan = request.user
        comment_obj.baiviet = topic
        comment_obj.ngaydangbinhluan = datetime.datetime.now()
        comment_obj.save()
        return HttpResponseRedirect(request.get_full_path()+"#guibinhluan")
    return render(request, 'pages/baiviet.html', {'Baiviet': topic, 'form': comment_form, 'binhluan': binhluan})
