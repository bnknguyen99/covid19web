from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from datetime import datetime

class Ngaygio(models.Model):
    idngay = models.AutoField(primary_key=True)
    ngaygio = models.DateTimeField(unique=True, blank=True, null=True)
    def __str__ (self):
        return self.ngaygio.strftime("%d/%m/%Y - %H:%M:%S ")
    class Meta:
        db_table = 'ngaygio'

class Chudebaiviet(models.Model):
    idchudebaiviet = models.AutoField(primary_key=True,)
    chude = models.CharField(max_length=50, unique= True,blank=True, null=True)
    def __str__ (self):
        return self.chude
    class Meta:
        db_table = 'chudebaiviet'


class Baiviet(models.Model):
    idbaiviet = models.AutoField(primary_key=True)
    tenbaiviet = models.CharField(db_column='tenBaiviet', max_length=500)  # Field name made lowercase.
    noidungbaiviet = models.TextField(db_column='noiDungBaiviet')  # Field name made lowercase.
    tomtat = models.TextField(blank=True, null=True)
    chudebaiviet = models.ForeignKey('Chudebaiviet', models.DO_NOTHING, db_column='chuDeBaiViet', to_field='chude')  # Field name made lowercase.
    hinhanh = models.CharField(db_column='hinhAnh', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tacgia = models.CharField(max_length=100, blank=True, null=True)
    ngaydangbaiviet = models.ForeignKey('Ngaygio', models.DO_NOTHING, db_column='ngayDangBaiViet',to_field='ngaygio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'baiviet'


class Binhluan(models.Model):
    idbinhluan = models.AutoField(primary_key=True)
    taikhoan = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='taikhoan', blank=True, null=True)
    baiviet = models.ForeignKey(Baiviet, models.DO_NOTHING, db_column='baiviet', blank=True, null=True,related_name='comments')
    noidungbinhluan = models.TextField()
    ngaydangbinhluan = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'binhluan'




