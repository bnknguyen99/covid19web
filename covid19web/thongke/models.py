from django.db import models
from datetime import datetime

class Ngaythang(models.Model):
    idngay = models.AutoField(primary_key=True)
    ngaythang = models.DateTimeField(unique=True, blank=True, null=True)
    def __str__(self):
        return self.ngaythang.strftime("%d/%m/%Y")
    class Meta:
        db_table = 'ngaythang'



class Dienbiendich(models.Model):
    iddienbiendich = models.AutoField(primary_key=True)
    tieude = models.CharField(max_length=100, blank=True, null=True, db_column='tieude')
    dienbien = models.TextField(db_column='dienbien')
    ngaycapnhat = models.ForeignKey('Ngaythang', models.DO_NOTHING, db_column='ngaycapnhat', to_field='ngaythang', blank=True, null=True)
    class Meta:
        db_table = 'dienbiendich'
    
class Tinhthanh(models.Model):
    idtinhthanh = models.AutoField(primary_key=True)
    tentinhthanh = models.CharField(unique=True, max_length=50, blank=True, null=True)
    def __str__(self):
        return self.tentinhthanh
    class Meta:
        db_table = 'tinhthanh'




class Diemtiemchung(models.Model):
    iddiadiem = models.AutoField(primary_key=True)
    tendiemtiem = models.CharField(max_length=100)
    sonha = models.CharField(max_length=100, blank=True, null=True)
    xaphuong = models.CharField(max_length=100, blank=True, null=True)
    quanhuyen = models.CharField(max_length=100, blank=True, null=True)
    tentinhthanh = models.ForeignKey('Tinhthanh', models.DO_NOTHING, db_column='tentinhthanh',to_field='tentinhthanh', blank=True, null=True)
    nguoiquanly = models.CharField(max_length=50, blank=True, null=True)
    sobantiem = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'diemtiemchung'

class Tinhhinhvaccine(models.Model):
    idvaccine = models.AutoField(primary_key=True)
    tentinhthanh = models.ForeignKey('Tinhthanh', models.DO_NOTHING, db_column='tentinhthanh', to_field='tentinhthanh', blank=True, null=True)
    khphanbo = models.IntegerField(blank=True, null=True)
    phanbothucte = models.IntegerField(blank=True, null=True)
    danso = models.IntegerField(blank=True, null=True)
    solieudatiem = models.IntegerField(blank=True, null=True)
    ngaycapnhat = models.ForeignKey(Ngaythang, models.DO_NOTHING, db_column='ngaycapnhat', to_field='ngaythang',blank=True, null=True)

    class Meta:
        db_table = 'tinhhinhvaccine'

class Tinhhinhcovid(models.Model):
    idcovid = models.AutoField(primary_key=True)
    tentinhthanh = models.ForeignKey('Tinhthanh', models.DO_NOTHING, db_column='tentinhthanh', to_field='tentinhthanh',blank=True, null=True)
    tongsoca = models.IntegerField(blank=True, null=True)
    homnay = models.CharField(max_length=7, blank=True, null=True)
    tuvong = models.IntegerField(blank=True, null=True)
    ngaycapnhat = models.ForeignKey(Ngaythang, models.DO_NOTHING, db_column='ngaycapnhat',to_field='ngaythang', blank=True, null=True)

    class Meta:
        db_table = 'tinhhinhcovid'

class TinhhinhcovidVn(models.Model):
    idcovid = models.AutoField(primary_key=True)
    tongsoca = models.IntegerField(blank=True, null=True)
    khoi = models.IntegerField(blank=True, null=True)
    tuvong = models.IntegerField(blank=True, null=True)
    ngaycapnhat = models.ForeignKey(Ngaythang, models.DO_NOTHING, db_column='ngaycapnhat',to_field='ngaythang', blank=True, null=True)

    class Meta:
        db_table = 'tinhhinhcovid_vn'

class TinhhinhcovidTg(models.Model):
    idcovid = models.AutoField(primary_key=True)
    tongsoca = models.IntegerField(blank=True, null=True)
    khoi = models.IntegerField(blank=True, null=True)
    tuvong = models.IntegerField(blank=True, null=True)
    ngaycapnhat = models.ForeignKey(Ngaythang, models.DO_NOTHING, db_column='ngaycapnhat',to_field='ngaythang', blank=True, null=True)

    class Meta:
        db_table = 'tinhhinhcovid_tg'