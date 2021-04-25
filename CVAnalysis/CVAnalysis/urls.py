"""CVAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cvmanager.views import homepage,contact,login,register,add,studentlogin,studentDash,about,companylogin,companyregister,companyverify,companyhome,signout,apply,applied,addesc,jobpost,algorithm

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    
    path('',homepage,name="homepage"),
    
    path('companyhome/',companyhome,name="companyhome"),
   
    path('companylogin/companyverify',companyverify,name="companyverify"),
    path('companylogin/companyregister',companyregister,name="companyregister"), 

    
    path('companylogin/algorithm',algorithm,name="algorithm"),
    path('companylogin/addesc',addesc,name="addesc"),
    path('companylogin/jobpost',jobpost,name="jobpost"),
    path('companylogin/',companylogin,name="companylogin"),

    #path('jobpost/',jobpost,name="jobpost"),
    path('about/',about,name="about"),
    path('studentDash/',studentDash,name="studentDash"),
    path('register/add/',add,name="add"),
    path('register/',register,name="register"),
    
    
    
    #path('addesc/jobpost',jobpost,name="jobpost"),
    
    #path('jobpost/',jobpost,name="jobpost"),
    #path('addesc/',addesc,name="addesc"),
    

    
    path('apply/applied',applied,name="applied"),    
    path('apply/',apply,name="apply"),
    path('contact/',contact,name="contact"),
    path('login/studentlogin',studentlogin,name="studentlogin"),
    path('login/',login,name="login"),
    path('signout/',signout,name="signout"),
    path('admin/', admin.site.urls),
    
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


    #urlpattern+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    #urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
