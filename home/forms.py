from django import forms
from .models import *

class otpform(forms.Form):
    Otp=forms.IntegerField(label='Otp',widget=forms.TextInput(attrs={'placeholder':'otp','class':'form-control'}))

class usercreateform(forms.Form):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'name'}))
    #Contact=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
    Address=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'address'}))
    cont=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
    #Contact=PhoneNumberField(label='',widgets=PhoneNumberField(attrs={'class':'form-control','placeholder':''}))
    Email=forms.EmailField(label="Email ID",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    Password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control'}))

class orderform(forms.ModelForm):
    class Meta:
        model=order
        fields=('fromplace','toplace','oEmail','oTime','weight',)
        #RecieverEmail=forms.EmailField(label="Email ID",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
        #numberv=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'place'}))
        fromplace=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'p'}))
        toplace=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'place'}))
        oEmail=forms.EmailField(label="Email ID",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
        #name=forms.CharField(label="Name",widget=forms.TextInput(attrs={
        #'class':'form-control','maxlength':'50','placeholder':'name'}))
        #r_pn=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cost'}))
        #oDate=forms.DateField(label='',widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date of birth'}))
        oTime=forms.DateTimeField(label='')
       # charge=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cost'}))
        # s_name=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'address'}))
        # m_name=forms.ModelChoiceField(queryset=media.objects.all())
        # v_name=forms.ModelChoiceField(queryset=vehicle.objects.all())
        weight=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'weight'}))

class vehicleform(forms.Form):
    # v_name=forms.ModelChoiceField(queryset=media.objects.all())
    # name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'50','placeholder':'name'}))
    vno=forms.CharField(label="vehicle No.",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'vehicle No.'}))
    vTime=forms.DateTimeField(label="Time")
    fromplace=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'p'}))
    toplace=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'place'}))

class mediaform(forms.Form):
    mname=forms.CharField(label="Name",widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'name'}))
    #Contact=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
    mAddress=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'address'}))
    mcont=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
    #Contact=PhoneNumberField(label='',widgets=PhoneNumberField(attrs={'class':'form-control','placeholder':''}))
    mEmail=forms.EmailField(label="Email ID",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    mPassword=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control'}))
    #reach=forms.CharField(label="reach",widget=forms.TextInput(attrs={
       # 'class':'form-control','maxlength':'50','placeholder':'name'}))
class selectform(forms.Form):
    n=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'select'}))
# from django import forms
# from .models import *

# class usercreateform(forms.Form):
#     name=forms.CharField(label="Name",widget=forms.TextInput(attrs={
#         'class':'form-control','maxlength':'50','placeholder':'name'}))
#     #Contact=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
#     Address=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'address'}))
#     #Contact=PhoneNumberField(label='',widgets=PhoneNumberField(attrs={'class':'form-control','placeholder':''}))
#     Email=forms.EmailField(label="Email ID",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
#     Password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control'}))

# class vehiclecreateform(forms.Form):
#     # c_num=forms.ForeignKey('c_num',on_delete=models.SET_NULL,null=True)
#     v_num=forms.CharField(label='v_num',widget=forms.TextInput(attrs={'class':'form-control','max_length':'10','placeholder':'vehicle number'}))
#     place1=forms.CharField(label='place1',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'from place'}))
#     place2=forms.CharField(label='place2',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'to place'}))
#     time1=forms.DateTimeField(label='time1',widget=forms.DateTimeInput(attrs={'class':'form-control','max_length':'13','placeholder':'departure time'}))
#     time2=forms.DateTimeField(label='time2',widget=forms.DateTimeInput(attrs={'class':'form-control','max_length':'13','placeholder':'arrival time'}))

# class courierbookform(forms.ModelForm):
#     class Meta:
#         model=courier
#         fields=('vehicle','weight')
#         vehicle=forms.ModelChoiceField(queryset=vehicle.objects.all())
#         weight=forms.FloatField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'10','placeholder':'weight'}))