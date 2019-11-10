from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.http import HttpResponse
from home.models import *
from home.forms import *
#import zerosms,requests
import json,random,re
from django.contrib import messages
#from django.core import mail
#import time
#from sinchsms import SinchSMS
# from gateway import Gateway
#from python_sms_gateway.nexmo import NexmoConnector
#from sms16.sms import Sms

#from twilio.rest import Client
#from django.conf import settings
# Create your views here.
#link= f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=k23h4kjh352kjh2k35j-234n234kjk-234mn23k4-234kkj&to={phone}&from=Ishwar&templatename=OTPBE&var1={name}&var2={otp_key}'

# requests.get(link)

def home_view(request):
    temp='/login/'
    temp1='/signup/'
    temp2='/loginM/'
    temp3='/signupM/'
    return render(request,"h.html",{"temp":temp,"temp1":temp1,"temp2":temp2,"temp3":temp3})

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def signup(request):
    if request.method=='POST':
        form=usercreateform(request.POST)
        #fm=otpform(request.POST)
        if form.is_valid():
            try:
                pat=user.objects.create(name=form.cleaned_data.get('name'),
                Email=form.cleaned_data.get('Email'),
                Address=form.cleaned_data.get('Address'),
                cont=form.cleaned_data.get('cont'),
                Password=form.cleaned_data.get('Password'),otpu=random.randint(10000,99999))#otpg=random.randint(10000,99999))
                if not re.match("^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]*", pat.name):
                    #return HttpResponse('invalid username')
                    messages.error(request,'invalid username')
                    return render(request,'create.html',{'form':form,'value':'signup'})
                flag = 0
                while True:
                    if (len(pat.Password)<8):
                        flag = -1
                        break
                    elif not re.search("[a-z]", pat.Password):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", pat.Password):
                        flag = -1
                        break
                    elif not re.search("[0-9]", pat.Password):
                        flag = -1
                        break
                    # elif not re.search("[_@$!*%#/\]", pat.Password):
                    #     flag = -1
                    #     break
                    elif re.search("\s", pat.Password):
                        flag = -1
                        break
                    else:
                        flag = 0
                        print("Valid Password")
                        break
                if flag ==-1:
                    print("Not a Valid Password") 
                    messages.error(request,'invalid password')
                    return render(request,'create.html',{'form':form,'value':'signup'})
                    
            #return HttpResponse("password should contain atleast one upper case,lower case,special character,number")
                print(pat.otpu)
                #pat.otpg=otpg
                URL = 'https://www.way2sms.com/api/v1/sendCampaign'
                print(URL)
                response = sendPostRequest(URL, 'VJPVF50BPMHFJN1HF4IA9CB3I5JURR05','E771DHCO9PKVB7Y5', 'stage', str(pat.cont), 'active-sender-id', 'your one time password is'+str(pat.otpu)+"dont share it" )
                name=request.session['name']=pat.name
                #otpg=request.session['otpg']=pat.otpg
                #return redirect('/otp/'+name+'/'+str(otpg))
                return redirect('/otp/'+name)
               
#pat=user.objects.create(otp=fm.cleaned_data.get('otp'))
                # if otpg==pat.otp:
                #     print('otp match')
                #     pat.save()
                #     name=request.session['name']=pat.name
                #     messages.success(request,'signed-up successfully')
                #     return redirect('/courier'+name)
                # else:                                
                #     print('otp doesnt match')
                #     messages.success(request,'invalid otp')
                #     return redirect('/admin')
            except ValueError:
                messages.error(request,'invalid contact number')
                return render(request,'create.html',{'form':form,'value':'signup'})
                #return HttpResponse('please enter correct contact number')
        else:    
            return render(request,'create.html',{'form':form,'value':'Signup'})
    else:
        form=usercreateform()
      #  fm=otpform()
        return render(request,'create.html' ,{'form':form,'value':'Signup'})

def signupM(request):
    if request.method=='POST':
        form=mediaform(request.POST)
        #fm=otpform(request.POST)
        if form.is_valid():
            try:
                pat=media.objects.create(mname=form.cleaned_data.get('mname'),
                mEmail=form.cleaned_data.get('mEmail'),
                mAddress=form.cleaned_data.get('mAddress'),
                mcont=form.cleaned_data.get('mcont'),
                mPassword=form.cleaned_data.get('mPassword'),motpu=random.randint(10000,99999))#otpg=random.randint(10000,99999))
                if not re.match("^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]*", pat.mname):
                    messages.error(request,'invalid username')
                    return render(request,'create.html',{'form':form,'value':'signup'})
                flag = 0
                while True:
                    if (len(pat.mPassword)<8):
                        flag = -1
                        break
                    elif not re.search("[a-z]", pat.mPassword):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", pat.mPassword):
                        flag = -1
                        break
                    elif not re.search("[0-9]", pat.mPassword):
                        flag = -1
                        break
                    # elif not re.search("[_@$!*%#/\]", pat.mPassword):
                    #     flag = -1
                    #     break
                    elif re.search("\s", pat.mPassword):
                        flag = -1
                        break
                    else:
                        flag = 0
                        print("Valid Password")
                        break
                if flag ==-1:
                    print("Not a Valid Password") 
                    messages.error(request,'invalid password')
                    return render(request,'create.html',{'form':form,'value':'signup'})
                print(pat.motpu)
                #pat.otpg=otpg
                URL = 'https://www.way2sms.com/api/v1/sendCampaign'
                print(URL)
                #response = sendPostRequest(URL, 'VJPVF50BPMHFJN1HF4IA9CB3I5JURR05','E771DHCO9PKVB7Y5', 'stage', str(pat.mcont), 'active-sender-id', 'your one time password is'+str(pat.motpu)+"dont share it" )
                mname=request.session['mname']=pat.mname
                #otpg=request.session['otpg']=pat.otpg
                #return redirect('/otp/'+name+'/'+str(otpg))
                return redirect('/otp/'+mname)
            except ValueError:
                messages.error(request,'invalid contact number')
                return render(request,'create.html',{'form':form,'value':'signup'})
        else:    
            return render(request,'create.html',{'form':form,'value':'Signup'})
    else:
        form=mediaform()
      #  fm=otpform()
        return render(request,'create.html' ,{'form':form,'value':'Signup'})

def otpver(request,name):
    if request.method=='POST':
        form=otpform(request.POST)
        if form.is_valid():
            oo=select.objects.create(n=form.cleaned_data.get('Otp'))
            u=user.objects.get(name=name)
            #oo.name=name
            #oo.save()
            #print('otp')
            #print(oo.otp)
            #print(otpg)
            print(oo.n)
            print(type(oo.n))
            print(u.otpu)
            print(type(u.otpu))
            if oo.n==u.otpu:
                messages.success(request,"create sucessfully!!")    
                temp='/courier/'+name
                return redirect(temp)
            else:
                return HttpResponse('wrong otp')
        else:    
            return render(request,'create.html',{'form':form,'value':'Signup'})
    else:
        form=otpform()
        return render(request,'create.html',{'form':form,'value':'Signup'})


def otpver(request,name):
    if request.method=='POST':
        form=otpform(request.POST)
        if form.is_valid():
            oo=select.objects.create(n=form.cleaned_data.get('Otp'))
            u=media.objects.get(name=name)
            #oo.name=name
            #oo.save()
            #print('otp')
            #print(oo.otp)
            #print(otpg)
            print(oo.n)
            print(type(oo.n))
            print(u.motpu)
            print(type(u.motpu))
            if oo.n==u.motpu:
                messages.success(request,"create sucessfully!!")    
                temp='/mediapage/'+name
                return redirect(temp)
            else:
                return HttpResponse('wrong otp')
        else:    
            return render(request,'create.html',{'form':form,'value':'Signup'})
    else:
        form=otpform()
        return render(request,'create.html',{'form':form,'value':'Signup'})

               

def login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        try:
            userlog=user.objects.get(name=username)
            if userlog:
                if userlog.Password==password:
                    #name=userlog.name
                    temp='/userpage/'+username
                    return redirect(temp)
                    #return HttpResponse('login success')
                else:
                    return HttpResponse('incorrect password')
        except user.DoesNotExist:
            userlog=None
            print('Someone tried to login and failed')
            print('they used username:{} password:{}'.format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        #return redirect('/admin')
        return render(request,'auth/login.html',{})

def Login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        try:
            userlog=media.objects.get(mname=username)
            if userlog:
                if userlog.mPassword==password:
                    #name=userlog.name
                    temp='/mediapage/'+username
                    return redirect(temp)   
                else:
                    return HttpResponse('incorrect password')
        except user.DoesNotExist:
            userlog=None
            print('Someone tried to login and failed')
            print('they used username:{} password:{}'.format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        #return redirect('/admin')
        return render(request,'auth/login.html',{})

def userpage(request,username):
    temp='/historyu/'+username
    temp1='/courier/'+username
    form=user.objects.filter(name=username)
    return render(request,'user.html',{'temp':temp,'temp1':temp1,'form':form})

def mediapage(request,username):
    g=media.objects.get(mname=username)
    print(g.id)
    temp='/history/'+str(g.id)
    temp1='/vehicle/'+username
    return render(request,'user.html',{'temp':temp,'temp1':temp1})

def Order(request,username):
    uname=user.objects.get(name=username)
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            pat=order.objects.create(fromplace=form.cleaned_data.get('fromplace'),toplace=form.cleaned_data.get('toplace'),oTime=form.cleaned_data.get('oTime'),oEmail=form.cleaned_data.get('oEmail'),r_pn=form.cleaned_data.get('r_pn'),charge=form.cleaned_data.get('charge'),s_name=form.cleaned_data.get('s_name'),
            m_name=form.cleaned_data.get('m_name'),v_name=form.cleaned_data.get('v_name')
            ,weight=form.cleaned_data.get('weight'))
            pat.numberv=''
            pat.charge=pat.weight*20
            pat.uname=uname.name
            if user.objects.filter(Email=pat.oEmail):
                pat.s_name=user.objects.get(Email=pat.oEmail)
                try:
                    x=vehicle.objects.filter(toplace=pat.toplace,fromplace=pat.fromplace)
                    temp='/select/'+str(pat.id)
                    pat.save()
                    return redirect(temp)
                    #pat.numberv=x[pat.n].vno
                except vehicle.DoesNotExist:
                    pat.numberv=None
                    b=order.objects.filter(id=pat.id)
                    return render(request,'home4.html',{'b':b})
            else:
                return HttpResponse('Sorry!... to inform this reciever is not the user of this website')
            #messages.success(request,"create sucessfully!!")    
            
            return redirect('/login')
        else:    
            return render(request,'home4.html',{'form':form})
    else:
        form=orderform()
        return render(request,'home4.html',{'form':form})

#media to inform about his journey
def Vehicle(request,username):
    uname=media.objects.get(mname=username)
    value=1
    if request.method=='POST':
        form=vehicleform(request.POST)
        if form.is_valid():
            pat=vehicle.objects.create(fromplace=form.cleaned_data.get('fromplace'),toplace=form.cleaned_data.get('toplace'),vTime=form.cleaned_data.get('vTime'),vno=form.cleaned_data.get('vno'))
            pat.name=uname.mname
            pat.reach="no"
            pat.save()
            #messages.success(request,"create sucessfully!!")    
            temp='/reach/'+str(pat.id)
            return redirect(temp)
        else:    
            return render(request,'home3.html',{'form':form,'value':value})
    else:
        form=vehicleform()
        return render(request,'home3.html',{'form':form,'value':value})

def Reach(request,id):
    uname=vehicle.objects.get(id=int(id))
    uname.reach="yes"
    uname.save()
    messages.success(request,"your activity is recorded")
    return redirect('/vehicle/'+uname.name)
    # return HttpResponse('Your activity is recorded')

def successOrder(request,username):
    uname=order.objects.get(uname=username)
    form=vehicle.objects.filter(toplace=uname.toplace,fromplace=uname.fromplace)
    return render(request,'home.html',{'form':form})

def Select(request,id):
    booked=order.objects.get(id=int(id))
    print('hi')
    print(booked.oTime.date())
    r=booked.oTime.strftime("%Y-%m-%d")
    id=int(id)
    available=vehicle.objects.filter(toplace=booked.toplace,fromplace=booked.fromplace,vTime__year=booked.oTime.year,vTime__day=booked.oTime.day,vTime__month=booked.oTime.month)
    if request.method=='POST':
        form=selectform(request.POST)
        if form.is_valid():
            pat=select.objects.create(n=form.cleaned_data.get('n'))
            try:
                search=vehicle.objects.get(id=pat.n)
                print("hi"+search.vno)
                
                g=vehicle.objects.get(id=pat.n)
                booked.numberv=g.vno
                booked.v_name=g
                booked.name=g.name
                #booked.m_name=vehicle.objects
                booked.save()
                pat.save()
            except vehicle.DoesNotExist:
                temp='/select/'+str(id)
                return redirect(temp)
            #messages.success(request,"create sucessfully!!")    
            
            return redirect('/login')
        else:    
            return render(request,'select.html',{'form':form,'available':available})
    else:
        form=selectform()
        return render(request,'select.html',{'form':form,'available':available})

def history(request,id):
    x=media.objects.get(id=int(id))
    r=x.mname
    print(x.mname)
    available=order.objects.filter(name=r)
    return render(request,'status.html',{'available':available})

def historyu(request,username):
    available=order.objects.filter(uname=username)
    return render(request,'home.html',{'available':available})

def Accept(request,id):
    uname=order.objects.get(id=int(id))
    uname.status="accepted"
    uname.save()
    messages.success(request,"your activity is recorded")
    return redirect('/loginM/')

def Reject(request,id):
    uname=order.objects.get(id=int(id))
    uname.status="rejected"
    uname.save()
    messages.success(request,"your activity is recorded")
    return redirect('/loginM/')




# from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
# from home.models import *
# from home.forms import *
# # Create your views here.
# def home_view(request):
#     temp='/login/'
#     return render(request,'home.html',{'temp':temp})

# def login(request):
#     if request.method=='POST':
#         username=request.POST.get('name')
#         password=request.POST.get('password')
#         try:
#             userlog=user.objects.get(name=username)
#             if userlog:
#                 if userlog.Password==password:
#                     #name=userlog.name
#                     #temp='/PatientPage/'+name
#                     #return redirect("/admin")
#                     return HttpResponse('login success')
#                 else:
#                     return HttpResponse('incorrect password')
#         except user.DoesNotExist:
#             userlog=None
#             print('Someone tried to login and failed')
#             print('they used username:{} password:{}'.format(username,password))
#             return HttpResponse("Invalid login details given")
#     else:
#         #return redirect('/admin')
#         return render(request,'auth/login.html',{})

# def signin(request):
#     if request.method=='POST':
#         form=usercreateform(request.POST)
#         if form.is_valid():
#             try:
#                 pat=user.objects.create(name=form.cleaned_data.get('name'),
#                 Email=form.cleaned_data.get('Email'),
#                 Address=form.cleaned_data.get('Address'),
#                 Contact=form.cleaned_data.get('Contact'),
#                 Password=form.cleaned_data.get('Password'))
#                 pat.save()
#             #name=request.session['patient_name']=pat.patient_name
#             #messages.success(request,"create sucessfully!!")    
#             #temp='/tokenT/'+name temp='/book/'
#                 return HttpResponse('sigin successful')
#             except ValueError:
#                 return HttpResponse('please enter correct contact number')
#         else:    
#             return render(request,'create.html',{'form':form,'value':'Signup'})
#     else:
#         form=usercreateform()
#         return render(request,'create.html',{'form':form,'value':'Signup'})

# def ve_create(request):
#     if request.method=='POST':
#         form=vehiclecreateform(request.POST)
#         if form.is_valid():
#             try:
#                 pat=vehicle.objects.create(v_num=form.cleaned_data.get('v_num'),
#                 place1=form.cleaned_data.get('place1'),
#                 place2=form.cleaned_data.get('place2'),
#                 time1=form.cleaned_data.get('time1'),
#                 time2=form.cleaned_data.get('time2'))
#                 pat.save()
#             #name=request.session['patient_name']=pat.patient_name
#             #messages.success(request,"create sucessfully!!")    
#             #temp='/tokenT/'+name temp='/book/'
#                 return HttpResponse('vehicle created successful')
#             except ValueError:
#                 return HttpResponse('please enter correct time')
#         else:
#             return render(request,'create.html',{'form':form,'value':'create vehicle'})

#     else:
#         form=vehiclecreateform()
#         return render(request,'create.html',{'form':form,'value':'Create vehicle'})

# def courier_book(request):
#     if request.method=='POST':
#         form=courierbookform(request.POST)
#         if form.is_valid():
#             pat=courier.objects.create(vehicle=form.cleaned_data.get('vehicle'),weight=form.cleaned_data.get('weight'))
#             pat.charges=pat.weight*10
#             pat.save()
#         #name=request.session['patient_name']=pat.patient_name
#         #messages.success(request,"create sucessfully!!")    
#         #temp='/tokenT/'+name temp='/book/'
#             return HttpResponse('courier booked successful')
#         else:
#             return render(request,'create.html',{'form':form,'value':'Book courier'})
#     else:
#         form=courierbookform()
#         return render(request,'create.html',{'form':form,'value':'Book courier'})
