from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ngaythang, list_display=('idngay', 'ngaythang'))
admin.site.register(Dienbiendich, list_display=('iddienbiendich', 'dienbien','ngaycapnhat'))
admin.site.register(Tinhthanh, list_display=('idtinhthanh', 'tentinhthanh'))
admin.site.register(Diemtiemchung, list_display=('iddiadiem', 'tendiemtiem','tentinhthanh'))
admin.site.register(Tinhhinhvaccine, list_display=('idvaccine', 'tentinhthanh','ngaycapnhat'), list_filter = ('tentinhthanh',), search_fields = ('tentinhthanh__tentinhthanh',))
admin.site.register(Tinhhinhcovid, list_display=('idcovid', 'tentinhthanh','ngaycapnhat'), list_filter = ('tentinhthanh',), search_fields = ('tentinhthanh__tentinhthanh',))
admin.site.register(TinhhinhcovidVn, list_display=('idcovid', 'ngaycapnhat'))
admin.site.register(TinhhinhcovidTg, list_display=('idcovid', 'ngaycapnhat'))