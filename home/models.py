from django.db import models
#from vininfo  import Vin
from django.utils import timezone
from datetime import date

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class user(models.Model):
    name=models.CharField('name',max_length=30,null=True)
    #Contact=PhoneNumberField('Contact',null=True)
    cont=PhoneNumberField('contact',null=True)
    Address=models.CharField('Address',max_length=200,null=True)
    Email=models.EmailField('Email',blank=False,null=True)#unique=true
    Password=models.CharField('password',max_length=20,null=True,blank=True)
    otpu=models.IntegerField('otp',null=True)
    #otpg=models.IntegerField('otp',null=True,blank=True)
    def __str__(self):
        return self.name


class Otpt(models.Model):
    name=models.CharField('name',max_length=30,null=True)
    Otp=models.IntegerField('otp',null=True)
    #otp=models.IntegerField('otp',null=True)

class media(models.Model):
    mname=models.CharField('name',max_length=30,null=True)
   # Contact=PhoneNumberField('Contact',null=True)
    mAddress=models.CharField('Address',max_length=200,null=True)
    mEmail=models.EmailField('Email',blank=False,null=True)#unique=true
    mPassword=models.CharField('password',max_length=20,null=True,blank=True)
    mcont=PhoneNumberField('contact',null=True)
    motpu=models.IntegerField('otp',null=True)
   # vnumber=models.Vin('vehicle number',null=True,blank=True)
    def __str__(self):
        return str(self.id)

class order(models.Model):
    #RecieverEmail=models.EmailField('reciever email',null=False)
    name=models.CharField('name',max_length=20,null=True,blank=True)
    status=models.CharField('accept/reject',max_length=20,null=True,blank=True)
    numberv=models.CharField('vehicle no.',max_length=20,null=True,blank=True)
    fromplace=models.CharField('From place',max_length=20,null=True,blank=True)
    toplace=models.CharField('To place',max_length=20,null=True,blank=True)
    oEmail=models.EmailField('Reciever Email',blank=False,null=True)#unique=true
    uname=models.CharField('name',max_length=20,null=True,blank=True)
    #rDate=models.DateTimeField(default=timezone.now )
    charge=models.FloatField('charge',null=True)
    #oDate=models.DateField('date')
    oTime=models.DateTimeField('time',null=True)
    weight=models.IntegerField('weight',null=True)
    r_pn=models.IntegerField('phonenumber',null=True)
    m_name=models.ForeignKey('media',on_delete=models.SET_NULL,null=True)
    v_name=models.ForeignKey('vehicle',on_delete=models.SET_NULL,null=True)
    s_name=models.ForeignKey('user',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.id)

class vehicle(models.Model):
    v_name=models.ForeignKey('media',on_delete=models.SET_NULL,null=True)
    name=models.CharField('name',max_length=30,null=True)
    vno=models.CharField('vehicle No.',max_length=20,null=True,blank=True)
    fromplace=models.CharField('From place',max_length=20,null=True,blank=True)
    toplace=models.CharField('To place',max_length=20,null=True,blank=True)
    vTime=models.DateTimeField('time',null=True)
    reach=models.CharField('reach',max_length=30,null=True)
    def __str__(self):
        return str(self.id)

class select(models.Model):
    n=models.IntegerField('number',null=True)
    def __str__(self):
        return str(self.id)
# from django.db import models
# #from phonenumber_field.modelfields import PhoneNumberField
# # Create your models here.
# class user(models.Model):
#     name=models.CharField('name',max_length=30,null=True)
#     #Contact=PhoneNumberField('Contact',null=True)
#     Address=models.CharField('Address',max_length=200,null=True)
#     Email=models.EmailField('Email',blank=False,null=True)#unique=true
#     Password=models.CharField('password',max_length=20,null=True,blank=True)
#     def __str__(self):
#         return self.name

# class vehicle(models.Model):
#     #c_num=models.ForeignKey('courier.id',on_delete=models.SET_NULL,null=True)
#     v_num=models.CharField('v_num',max_length=10,null=True)
#     place1=models.CharField('from place',max_length=10,null=True)
#     place2=models.CharField('to place',max_length=10,null=True)
#     time1=models.DateTimeField('from time',max_length=13,null=True)
#     time2=models.DateTimeField('to time',max_length=13,null=True)
#     def __str__(self):
#         return self.v_num

# class courier(models.Model):
#     vehicle=models.ForeignKey('vehicle',on_delete=models.SET_NULL,null=True)
#     weight=models.FloatField('weight',max_length=10,null=True)
#     charges=models.FloatField('charges',max_length=10,null=True)