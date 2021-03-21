from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import CompanyDetail
from django.contrib.sessions.models import Session 

# Create your views here.
from django.contrib import messages
def homepage(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def register(request):
    
    
    return render(request,"register.html")
def add(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        try:
            flag=User.objects.get(username=username)
            flag2=User.objects.get(email=email)
            messages.info(request,"User already exists")
            return redirect("register")
            
            
        except User.DoesNotExist:
            if(password1==password2 and len(password1)>=5):
                user=User.objects.create_user(first_name=name,password=password1,email=email,username=username)
                user.save()
                print("user created")
                return redirect('login')
            else:
                print("Check your credentials")
                return redirect("/")
           


def companyregister(request):
    
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        state=request.POST['state']
        zipcode=request.POST['zip']
        city=request.POST['city']
        address1=request.POST['address1']

        address2=request.POST['address2']
        record=CompanyDetail(email=email,password=password,address1=address1,address2=address2,state=state,city=city,zipcode=zipcode)    
        record.save()
        return render(request,"CompanyLogin.html")
          

def companyverify(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        #company=auth.authenticate(email=email,password=password)
        
        is_companymail=CompanyDetail.objects.filter(email=email).exists()
        is_companypass=CompanyDetail.objects.filter(password=password).exists()
        if(is_companymail and is_companypass):
            #auth.login(request,email)
            return render(request,"CompanyDashboard.html")
        else:
            print("impossible")
            messages.info(request,"Invalid Credentials")
            return redirect("companylogin")

def companyhome(request):
    return render(request,"CompanyHome.html")

def studentlogin(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        user=auth.authenticate(username=username,password=password)
        if(user!=None):
            request.session['is_logged']=True
            request.session['email']=email
            request.session['username']=username
            auth.login(request,user)
            print("user exists")
            return render(request,"studentHome.html")
        else:
            messages.info(request,"invalid credentials")
            print("no user")
            return redirect("login")
def studenthome(request):
    if(request.session.has_key('is_logged')):
        return render(request,"studentHome.html")
    return redirect("login")
def studentDash(request):
    
    return render(request,"studentDash.html",{'email':request.session['email'],'user':request.session['username']})

def about(request):
    return render(request,"AboutUs.html")

def companylogin(request):
    return render(request,"CompanyLogin.html")

def signout(request):
    auth.logout(request)
    #request.session['is_logged']=False
    return render(request,"login.html")