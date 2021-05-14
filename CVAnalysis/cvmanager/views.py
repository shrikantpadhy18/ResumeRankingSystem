from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import CompanyDetail,appliedDetail,jobdesc,queryform
from django.contrib.sessions.models import Session 
import PyPDF2
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfTransformer 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
                request.session['name']=name
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
            request.session["cmpemail"]=email
            request.session['cmplogged']=True
            print(request.session["cmpemail"])
            return render(request,"CompanyDashboard.html",{'email':email,'flage':False})
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

            request.session['first_name']=User.objects.filter(email=email).values('first_name').first()['first_name']    
            #request.session['name']=name
            print("firstname",request.session['first_name'])
            auth.login(request,user)
            print("user exists")

            #fetch all job desc made by companies
            data=list(jobdesc.objects.all())
            #list of dictionaries that would contain the dictionary of job desc 
            print(data)
            for i in data:
                print(i.database)

            return render(request,"studentHome.html",{'data':data})
        else:
            messages.info(request,"invalid credentials")
            print("no user")
            return redirect("login")
def studenthome(request):
    if(request.session.has_key('is_logged')):
        return render(request,"studentHome.html")
    return redirect("login")

def studentDash(request):
    if(request.session.has_key('is_logged')):
        first_name=User.objects.filter(email=request.session['email']).values('first_name').first()['first_name']
        last_name=User.objects.filter(email=request.session['email']).values('last_name').first()['last_name']
        
        return render(request,"studentDash.html",{'email':request.session['email'],'user':request.session['username'],'Name':first_name+" "+last_name})
    return redirect("login")
def about(request):
    return render(request,"AboutUs.html")

def companylogin(request):
    return render(request,"CompanyLogin.html")

def signout(request):
    auth.logout(request)
    request.session['is_logged']=False
    request.session['email']=None
    request.session['username']=None
    request.session['first_name']=None
    return render(request,"home.html")

def apply(request):
    if(request.session.has_key('is_logged')):
        return render(request,"apply.html",{'email':request.session['email'],'name':request.session['first_name']})
    return redirect("login")
def applied(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["phone"]
        gender=request.POST["gender"]
        file=request.FILES["file"]
        #resumepath="C://Users//shrikant padhy//Desktop//Path//"+request.session['username']
        record=appliedDetail(name=name,email=email,mobile=mobile,gender=gender,resumepath=file)
        #print(request.session['username'])
        record.save()

        return redirect("apply")

#addesc actually handles the get request of adding description tag made by the company,it return the description tag page where the tags will be created
def addesc(request):
    if(request.method=="GET" and request.session['cmplogged']==True):

        return render(request,"RequireMentForm.html",{'cmpemail':request.session['cmpemail']})

#below view actually is used for storing the job post made by the company into the database.
def jobpost(request):
    if(request.method=="POST"):
        language=request.POST["language"]
        Frameworks=request.POST["Frameworks"]
        Database=request.POST["database"]
        experience=request.POST["experience"]
        companyname=request.POST["companyname"]
        jobrole=request.POST["role"]
        batch=request.POST["batch"]
        startdate=request.POST["startdate"]
        enddate=request.POST["enddate"]
        companyid=request.POST["cid"]
        record=jobdesc(programmingL=language,database=Database,frameworks=Frameworks,Experience=experience,name=companyname,role=jobrole,batch=batch,registrationstart=startdate,registrationend=enddate,cid=companyid)
        record.save()
        print("description submitted")

        return redirect("addesc")
def algorithm(request):
    if(request.session['cmplogged']==True):
        #the below path represent the directory in which all the uploaded documents would get stored
        path="C:\\Users\shrikant padhy\\Desktop\\finaleyear\\ResumeRankingSystem\\CVAnalysis\\media\\media"
        ans=[]
        res=[]
        #ans array represnt the all the files present in the given path
        #we will iterate over all the files present in our directory one by one and convert the pdf to text and stores them in one array res which will reperesent the array of resumes 
        
        for root,dirs,files in os.walk(path):
            ans=files
        
            #files=open(files,'rb')
            '''pdfread=PyPDF2.PdfFileReader(files)
            st=""
            for i in range(pdfread.getNumPages()):
                page=pdfread.getPage(i)

                pageContent=page.extractText()
                st+=str(pageContent)
            ans.append(st)'''
        for i in ans:
            #pyPDF2 will be used to convert the pdf to text 
            pdfread=PyPDF2.PdfFileReader(path+"\\"+str(i))
            st=""
            #in each pdf there will be multiple pages so we access them one by one using below loop and store them under one single variable st ,once the loop is finished st will now hold all the pages.which can be stored in the list 
            for j in range(pdfread.getNumPages()):
                page=pdfread.getPage(j)

                pageContent=page.extractText()
                st+=str(pageContent)
            res.append([st,path+"\\"+str(i)])

        print(res)

        ob=jobdesc.objects.filter(cid=request.session['cmpemail'])    
        print(ob)
        #the below varibale will hold the job description posted by the company that would contain5 parameters based on which the CV will be ranked
        st=""

        for i in ob:
            st+=str(i.programmingL)
            st+=" "
            st+=str(i.database)
            st+=" "
            st+=str(i.frameworks)
            st+=" "
            st+=str(i.Experience)
            st+=" "
            st+=str(i.role)
            st+=" "
        #will store the match percent of resumes

        matchpercent=[]    
        for i in res:
            test=[i[0],st]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(test)

            #tfidf section
            tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
            tfidf_transformer.fit(count_matrix)
            #count matrix for tfidf transformer
            count_vector=cv.transform(list(i[0]))
            print("count_vector",count_vector)
            #tfidf scores
            tfidf_vector=tfidf_transformer.transform(count_vector)
            #print("tfidf vector",tfidf_vector)
            print("cosine similarity of tfidf vector",cosine_similarity(tfidf_vector))


            ###########
            print("cosine similarity",cosine_similarity(count_matrix))
            print()
            respath="media/"+str(i[1]).split("media\\")[2] #resume path is present in this format inise the table cvmanager_applieddetail.by using this we will fetch the email of the candidate
            Email=appliedDetail.objects.filter(resumepath=respath).values('email')
            dataEmail=None
            if(Email):
                dataEmail=Email[0].get('email',None)
            #matchparent contains 4 field percentage match,resumepath in computer,resume name,email of candidate        
            x=0
            print("x",x)
            x=round(cosine_similarity(count_matrix)[0][1]*100*5,2)
            matchpercent.append([x,i[1],str(i[1]).split("media\\")[2],dataEmail])
            sendmailtorejected=list(filter(lambda n:n[0]<50,matchpercent))
            print("sendemail",sendmailtorejected)
            if(len(sendmailtorejected)>0):
                print(len(sendmailtorejected))
                #Send mail to rejected candidates
                fromaddr="prashantpadhy21@gmail.com"
                msg=MIMEMultipart()
                msg['from']=fromaddr
                msg['subject']="UPDATE REGARDING OFF CAMPUS DRIVE"
                body="THE BELOW WAS OUR REQUIREMENT\n"+st
                msg.attach(MIMEText(body,'plain'))
                server=smtplib.SMTP('smtp.gmail.com',port=587)
                server.starttls()#connection established with gmail
                server.login(fromaddr,"21052003")
                    
                for i in sendmailtorejected:
                    msg['to']=i[3]
                    text=msg.as_string()
                    server.sendmail(fromaddr,i[3],text)
                server.quit() 

        #d=dict()

        print(matchpercent)
        fun=lambda n:n[0]
        matchpercent.sort(key=fun,reverse=True)
        
        return render(request,"CompanyDashboard.html",{'email':request.session['cmpemail'],'flag':True,'matchpercent':matchpercent})
def cmplogout(request):
    request.session['cmpemail']=None
    request.session['cmplogged']=None
    return render(request,"home.html")

def griev(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        email=request.POST["email"]
        msg=request.POST["message"]

        record=queryform(name=name,email=email,message=msg)
        record.save()

        return render(request,"contact.html")

        