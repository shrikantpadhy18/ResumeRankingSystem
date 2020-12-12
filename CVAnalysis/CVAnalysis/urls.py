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
from cvmanager.views import homepage,contact,login,register,add,studentlogin,studentDash,about,companylogin,companyregister,companyverify,companyhome

urlpatterns = [

    path('',homepage,name="homepage"),
    path('companyhome/',companyhome,name="companyhome"),
    path('companylogin/companyverify',companyverify,name="companyverify"),
    path('companylogin/companyregister',companyregister,name="companyregister"), 
    path('companylogin/',companylogin,name="companylogin"),
   
    path('about/',about,name="about"),
    path('studentDash/',studentDash,name="studentDash"),
    path('register/add/',add,name="add"),
    path('register/',register,name="register"),
    
    path('contact/',contact,name="contact"),
    
    path('login/studentlogin',studentlogin,name="studentlogin"),
    path('login/',login,name="login"),
    
    path('admin/', admin.site.urls),
]
