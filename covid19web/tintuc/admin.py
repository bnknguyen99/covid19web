from django.contrib import admin
# Register your models here.
from .models import *

class CommentInline(admin.TabularInline):
    model = Binhluan
        
admin.site.register(Ngaygio, list_display = ('idngay','ngaygio'))
admin.site.register(Chudebaiviet, list_display = ('idchudebaiviet', 'chude'))
#admin.site.register(Baiviet, list_display = ('idbaiviet', 'tenbaiviet', 'ngaydangbaiviet'))
admin.site.register(Binhluan)


class BaivietAdmin(admin.ModelAdmin):
    list_display = ['tenbaiviet', 'ngaydangbaiviet']
    list_filter = ['tenbaiviet']
    search_fields = ['tenbaiviet']
    inlines = [CommentInline]
 
admin.site.register(Baiviet, BaivietAdmin)