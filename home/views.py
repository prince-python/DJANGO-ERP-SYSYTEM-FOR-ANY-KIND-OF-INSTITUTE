from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Course,Student,Amount
import datetime
def index(request):
    if request.method=='POST':
        sname=request.POST['sname']
        email=request.POST['email']
        mob=request.POST['mob']
        branch=request.POST['branch']
        cr=request.POST.getlist('course')
        status=request.POST['status']
        date=datetime.datetime.now()
        address=request.POST['address']
        qualification=request.POST['qualification']
        sem=request.POST['sem']
        p=request.POST['passout']
        for i in cr:
            course=Course.objects.get(id=i)
        passout=int(p)
        Student.objects.create(sname=sname,email=email,mob=mob,branch=branch,status=status,date=date,address=address,
                               sem=sem,qualification=qualification,passout=passout,course=course,doe=date)
        messages.info(request,'student added sucessfully')
        return render(request,'index.html')
    else:
        cr=Course.objects.all()
        return render(request,'index.html',{'cr':cr})
    
    
    
    
    
def addcourse(request):
    if request.method=='POST':
        c=Course()
        c.cname=request.POST['cname']
        c.duration=request.POST['duration']
        c.details=request.POST['details']
        f=request.POST['fees']
        c.fees=int(f)
        c.save()
        messages.info(request,'course added sucessfully')
        return redirect('/')
    else:
        return render(request,'addcourse.html')
    
    
    
    
    
def showcourse(request):
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})




def showstudents(request):
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})















def payamount(request):
    if request.method=='POST':
        a=Amount()
        id=request.POST['student']
        st=Student.objects.get(id=id)
        a.student=st
        tf=request.POST['tf']
        a.total_fee=int(tf)
        submitamount=request.POST['submitamount']
        sb=Amount.objects.filter(student_id=id).all()
        if len(sb)>0:
            a.submitdate=sb[0].submitdate+','+str(datetime.datetime.now())
            sb=sb[0].submitamount
            a.submitamount=sb+','+submitamount
            tt=sb.split(",")
            ss=0
            for i in tt:
                ss=ss+int(i)
            a.remaining=int(tf)-ss-int(submitamount)
        else:
            a.submitamount=submitamount
            a.remaining=int(tf)-int(submitamount)
            a.submitdate=datetime.datetime.now()
        a.nextpaydate=request.POST['nextpaydate']
        a.save()
        st=Student.objects.all()
        return render(request,'payamount.html',{'st':st})
    else:
        st=Student.objects.all()
        return render(request,'payamount.html',{'st':st})
    
    
  
  
  
  
  
  
    
    
    
    
def showam(request):
    id=request.GET['val']
    t=Student.objects.get(id=id)
    s=Amount.objects.filter(student=t).all()
    rm=0
    his=[['no','records found']]
    if len(s)>0:
        rm=s[0].remaining
        l1=s[0].submitamount.split(",")
        l2=s[0].submitdate.split(",")
        his=list(zip(l1,l2))
    else:
        rm=t.course.fees
    return render(request,'showajax.html',{'totalfee':t.course.fees,'rm':rm,'his':his})



def searchenquiry(request):
    if request.method=='POST':
        cid=request.POST['course']
        status=request.POST['status']
        sname=request.POST['sname']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=Student.objects.all()
        if fdt and tdt is not '':
            st=st.filter(doe__range=(fdt, tdt))
        if sname is not '':
            st=st.filter(sname=sname)
        if status is not '':
            st=st.filter(status=status)
        if cid is not   '':
            st=st.filter(course=cid)
        return render(request,'showstudents.html',{'st':st})
    else:
        cr=Course.objects.all()
        return render(request,'searchenquiry.html',{'cr':cr})
    
    
def studentdelete(request,id):
    id=Student.objects.get(id=id)
    id.delete()
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})


def cdelete(request,id):
    id=Course.objects.get(id=id)
    id.delete()
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})







def studentupdate(request,id):
        st=Student.objects.filter(id=id)
        cr=Course.objects.all()
        return render(request,'studentupdate.html',{'st': st ,'cr':cr})
    

def cupdate(request,id):
    
        cr=Course.objects.filter(id=id)
        return render(request,'courseupdate.html',{'cr':cr})
def cupdates(request,id):
    if request.method == 'POST':
        
        i=request.POST['id']
        cname=request.POST['name']
        duration=request.POST['duration']
        details=request.POST['details']
        f=request.POST['fees']
        fees=int(f)
        c= Course(id=i,cname=cname,duration=duration,details=details,fees=fees)
        c.save()
        messages.info(request,'course added sucessfully')
        cr=Course.objects.all()
        return render(request,'showcourse.html',{'cr':cr})  
        

    
    
def studentupdatesave(request,id):
    if request.method=='POST':
        id=request.POST['id']
        sname=request.POST['sname']
        email=request.POST['email']
        mob=request.POST['mob']
        branch=request.POST['branch']
        cr=request.POST.getlist('course')
        status=request.POST['status']
        date=datetime.datetime.now()
        address=request.POST['address']
        qualification=request.POST['qualification']
        sem=request.POST['sem']
        p=request.POST['passout']
        for i in cr:
            course=Course.objects.get(id=i)
        passout=int(p)
        s=Student(id=id,sname=sname,email=email,mob=mob,branch=branch,status=status,date=date,address=address,
                               sem=sem,qualification=qualification,passout=passout,course=course,doe=date)
        s.save()
        messages.info(request,'student added sucessfully')
        st=Student.objects.all()
        return render(request,'showstudents.html',{'st':st})
    else:
        cr=Student.objects.all()
        return render(request,'studentupdate.html',{'cr':cr})