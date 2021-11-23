from django.urls import path

from . import views

urlpatterns =[
    path('', views.covid.as_view(), name = 'thongke'),
    path('dienbiendich', views.dienbiendich.as_view(), name = 'dienbiendich'),
    path('tinhhinhcovid', views.covid.as_view(), name = 'tinhhinhcovid'),
    path('thongtintiemchung', views.vaccine.as_view(), name = 'thongtintiemchung'),

]