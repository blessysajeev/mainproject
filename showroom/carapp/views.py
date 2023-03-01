from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

def index(request):  
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']      
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:   
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('register.html') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('register.html') 
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                u=customer(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                u.save();
            print("User Created");
            messages.success(request,"successfully registered")
            return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    # request.session.flush()
    # if 'username' in request.session:
    #     return redirect('home.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=authenticate(username=username,password=password)
    

        if user:
            print(2)
            auth.login(request,user)
            #save email in session
            request.session['username'] = username
            

            return redirect('home')
        else:
            # print(3)
            messages.info(request,"invalid values")
            return redirect('login')     
    return render(request,'login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')    

def home(request):
    if 'username' in request.session:
        username=request.session['username']
        obj=Vehicles.objects.all()
        object={'result':obj,'name':username}
        return render(request,'home.html',object)
    return redirect('login')

def testdrive(request):  
    obj={}
    obj=Vehicles.objects.all()
    context={'result':obj}

    # objtime={}
    # objtime=time.objects.all()
    # cont={'res':objtime}

    if request.method=='POST':
        
        username=request.session['username']
        user=customer.objects.filter(username=username)
        
        for i in user:
            id=i.id
            print(id)
        
        venue=request.POST['venue']
        carmodel=request.POST['carmodel']  
        Contact=request.POST['Contact']  
        Email=request.POST['Email']  
        testdate=request.POST['testdate']
        testtime=request.POST['testtime']
        # print(username,user,venue,carmodel,Contact,Email,testdate,testtime)
        # print('userid',id)
        # print(Contact)
        
        test=test_drive(username_id=id,venue=venue,carmodel=carmodel,testdate=testdate,testtime=testtime,Contact=Contact,Email=Email)
        # num=customer(Contact=Contact)
        # num.save()
        test.save()
        messages.success(request, "book appoinment successfully.")
    return render(request,'testdrive.html',context)

def Cars(request):
    obj={}
    obj=Vehicles.objects.all()
    context={'result':obj}
    return  render(request, 'cars.html',context)

def singleCar(request, id):
    print(id)
    lst=Vehicles.objects.filter(id=id)
    context={
        'lst':lst
    }
    return render(request, 'singleCar.html',context)

def testview(request):
    obj=test_drive.objects.all()
    # context={'info':obj}
    return render(request,'testview.html',
    {'obj':obj})

def delete(request,id):
    appoimnt_info=test_drive.objects.get(id=id)
    appoimnt_info.delete()
    return redirect('testview')