from django.urls import path
from . import views
urlpatterns =[
    path('', views.hienthibaiviet.as_view(), name='tintuc'),
    path('<int:pk>', views.post_comments_controller, name = 'baiviet')
    
]