import smtplib

from django.shortcuts import render,redirect
from django.shortcuts import render
from django.urls import reverse

from django.core.files.storage import FileSystemStorage
import os
from ca_proj.settings import BASE_DIR


# Create your views here.
from ca_client.models import login, userregistration, client_details, account_details, firm_details, audit_types, filing_date, client_type, intimation, document_detail, audit_request



def index(request):
    return render(request,'index.html')





def register(request):
    return render(request,'register.html')

def logcheck(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        request.session['username']=username

        checklogin = login.objects.filter( username=username).values()
        for a in checklogin:
            utype = a['type']
            upass= a['password']
            if(upass == password):
                if (utype == "ca"):
                    return render(request, 'accountent_home.html', context={'msg': 'welcome to storehead'})

                if(utype == "admin"):
                    return render(request, 'admin_home.html', context={'msg': 'welcome to customer'})

                if (utype == "client"):
                    return render(request, 'client_home.html', context={'msg': 'welcome to account dept'})

            else:
                return render(request,'login.html',{'msg':'Check user name or passwrod'})

    return render(request,'login.html')

def insertuserregistration(request):
    if request.method=="POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        email = request.POST.get('t3', '')
        mobilenumber = request.POST.get('t4', '')
        userregistration.objects.create(username=username, password=password, email=email,
                                     mobilenumber=mobilenumber)

    return render(request,'userregistration.html')


def deleteuserregistration(request,pk):
    id=userregistration.objects.get(id=pk)
    id.delete()
    userdict=userregistration.objects.all()
    return render(request, 'viewuserregistration.html',{'userdict':userdict})

def viewuserregistration(request):
    userdict=userregistration.objects.all()
    return render(request, 'viewuserregistration.html',{'userdict':userdict})





def insertclient_details(request):
    if request.method == "POST":
        ctype = request.POST.get('t11', '')

        client_id = request.POST.get('t1', '')

        ctype=ctype[0:4]
        ci=client_id

        clientid=ctype+ci
        client_name = request.POST.get('t2', '')
        pan = request.POST.get('t3', '')
        mobile = request.POST.get('t4', '')
        email_id = request.POST.get('t5', '')
        address = request.POST.get('t6', '')
        aadhar_no = request.POST.get('t7', '')
        start_date = request.POST.get('t8', '')
        client_details.objects.create(client_id=clientid, client_name=client_name, pan=pan,
                                            mobile=mobile, email_id=email_id, address=address, aadhar_no=aadhar_no,
                                         start_date=start_date )


        base_url = reverse('insertaccount_details')
        return redirect(base_url)

    p = client_details.objects.all().order_by('id').last()
    pid = int(p.id) + 1
    return render(request, 'client_details.html',{'pid':pid})

def deleteclientdetails(request,pk):
    id=client_details.objects.get(id=pk)
    id.delete()
    userdict=client_details.objects.all()
    return render(request, 'viewclientdetails.html',{'userdict':userdict})


def viewclientdetails(request):
    userdict=client_details.objects.all()
    return render(request, 'viewclientdetails.html',{'userdict':userdict})




def insertaccount_details(request):
    if request.method == "POST":
        client_id = request.POST.get('t1', '')
        account_no = request.POST.get('t2', '')
        bank_name = request.POST.get('t3', '')
        ifsc = request.POST.get('t4', '')
        account_details.objects.create(client_id=client_id, account_no=account_no, bank_name=bank_name,
                                            ifsc=ifsc)
        base_url = reverse('insertfirm_details')
        return redirect(base_url)

    return render(request, 'account_details.html')

def deleteaccdetails(request,pk):
    id=account_details.objects.get(id=pk)
    id.delete()
    userdict=account_details.objects.all()
    return render(request, 'viewaccdetails.html',{'userdict':userdict})



def viewaccdetails(request):
    userdict=account_details.objects.all()
    return render(request, 'viewaccountdetails.html',{'userdict':userdict})




def insertfirm_details(request):
    if request.method == "POST":
        firm_id = request.POST.get('t1', '')
        firm_name = request.POST.get('t2', '')
        client_id = request.POST.get('t3', '')
        website = request.POST.get('t4', '')
        address = request.POST.get('t5', '')
        cin = request.POST.get('t6', '')
        firm_details.objects.create(firm_id=firm_id, firm_name=firm_name, client_id=client_id,
                                            website=website, address=address, cin=cin)

        return render(request, 'accountent_home.html')

    return render(request, 'firm_details.html')


def deletefirmdetails(request,pk):
    id=firm_details.objects.get(id=pk)
    id.delete()
    userdict=firm_details.objects.all()
    return render(request, 'viewfirmdetails.html',{'userdict':userdict})



def viewfirmdetails(request):
    userdict=firm_details.objects.all()
    return render(request, 'viewfirmdetails.html',{'userdict':userdict})



def insertaudit_type(request):
    if request.method == "POST":
        audit_id = request.POST.get('t1', '')
        audit_type = request.POST.get('t2', '')
        audit_month = request.POST.get('t3', '')
        start_date = request.POST.get('t4', '')
        end_date = request.POST.get('t5', '')
        fees = request.POST.get('t6', '')
        audit_types.objects.create(audit_id=audit_id, audit_type=audit_type, audit_month=audit_month,
                                            start_date=start_date, end_date=end_date, fees=fees)

    return render(request, 'audit_types.html')

def deleteaudittypes(request,pk):
    id=audit_types.objects.get(id=pk)
    id.delete()
    userdict=audit_types.objects.all()
    return render(request, 'viewaudittypes.html',{'userdict':userdict})


def viewaudittypes(request):
    userdict=audit_types.objects.all()
    return render(request, 'viewaudittypes.html',{'userdict':userdict})



def insertfiling_date(request):
    if request.method == "POST":
        filing_id = request.POST.get('t1', '')
        filing_type = request.POST.get('t2', '')
        start_date = request.POST.get('t3', '')
        end_date = request.POST.get('t4', '')
        filing_date.objects.create(filing_id=filing_id, filing_type=filing_type,
                                            start_date=start_date, end_date=end_date)

    return render(request, 'filing_date.html')


def deletefilingdate(request,pk):
    id=filing_date.objects.get(id=pk)
    id.delete()
    userdict=filing_date.objects.all()
    return render(request, 'viewfilingdate.html',{'userdict':userdict})


def viewfilingdate(request):
    userdict=filing_date.objects.all()
    return render(request, 'viewfilingdate.html',{'userdict':userdict})



def insertclient_type(request):
    if request.method == "POST":
        client_id = request.POST.get('t1', '')
        client_types = request.POST.get('t2', '')
        pan = request.POST.get('t3', '')
        license_number = request.POST.get('t4', '')
        client_type.objects.create(client_id=client_id, client_type=client_types, pan=pan, license_number=license_number)

    return render(request, 'client_types.html')

def deleteclienttypes(request,pk):
    id=client_type.objects.get(id=pk)
    id.delete()
    userdict=client_type.objects.all()
    return render(request, 'viewclienttypes.html',{'userdict':userdict})



def viewclienttypes(request):
    userdict=client_type.objects.all()
    return render(request, 'viewclienttypes.html',{'userdict':userdict})


def insertintimation(request):
    if request.method == "POST":
        client_id = request.POST.get('t1', '')
        intimation_type = request.POST.get('t2', '')
        date = request.POST.get('t3', '')
        subject = request.POST.get('t4', '')
        details = request.POST.get('t5', '')

        intimation.objects.create(client_id=client_id, intimation_type=intimation_type,
                                            date=date, subject=subject, details=details)
        upass = subject
        content = upass
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('caclient20@gmail.com', 'szjxhpeezrpxeiek')
        mail.sendmail('caclient20@gmail.com', client_id, content)
        mail.close()
        # messages.success(request, 'Your password has been sent to your email')
        return render(request, 'intimation.html')
    return render(request, 'intimation.html')

def deleteintimation(request,pk):
    id=intimation.objects.get(id=pk)
    id.delete()
    userdict=intimation.objects.all()
    return render(request, 'viewintimation.html',{'userdict':userdict})





def viewintimation(request):
    userdict=intimation.objects.all()
    return render(request, 'viewintimation.html',{'userdict':userdict})



def insertdocument_detail(request):
    if request.method == "POST":
        client_id = request.POST.get('t1', '')
        document_id = request.POST.get('t2', '')
        document_name = request.POST.get('t3', '')
        uplaod_date = request.POST.get('t4', '')
        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        document_detail.objects.create(client_id=client_id, document_id=document_id,
                                            document_name=document_name, uplaod_date=uplaod_date, url=myfile)

        return render(request, 'document_details.html')

    return render(request, 'document_details.html')


def deletedocumentdetails(request,pk):
    id=document_detail.objects.get(id=pk)
    id.delete()
    userdict=document_detail.objects.all()
    #print("file can not be deleted")
    return render(request, 'viewdocumentdetails.html',{'userdict':userdict})


def viewdocdetails(request):
    userdict=document_detail.objects.all()
    return render(request, 'viewdocumentdetails.html',{'userdict':userdict})




def insertaudit_request(request):
    if request.method == "POST":
        firm_id = request.POST.get('t1', '')
        request_id = request.POST.get('t2', '')
        audit_type = request.POST.get('t3', '')
        request_status = request.POST.get('t4', '')
        status = request.POST.get('t5', '')
        audit_request.objects.create(firm_id=firm_id, request_id=request_id,
                                            audit_type=audit_type, request_status=request_status, status=status)

    return render(request, 'audit_request.html')

def deleteauditrequest(request,pk):
    id=audit_request.objects.get(id=pk)
    id.delete()
    userdict=audit_request.objects.all()
    return render(request, 'viewauditrequest.html',{'userdict':userdict})



def viewauditrequest(request):
    userdict=audit_request.objects.all()
    return render(request, 'viewauditrequest.html',{'userdict':userdict})


def insertaccountent(request):
    if request.method == "POST":
        accountet_id = request.POST.get('t1', '')
        name = request.POST.get('t2', '')
        address = request.POST.get('t3', '')
        qualification = request.POST.get('t4', '')
        experience = request.POST.get('t5', '')
        mobile_no = request.POST.get('t5', '')
        audit_request.objects.create(accountet_id=accountet_id, name=name,
                                            address=address, qualification=qualification, experience=experience, mobile_no=mobile_no)

    return render(request, 'accountent.html')


def accountent_menu(request):
    return render(request, 'viewauditrequest.html')

def accountent_home(request):
    return render(request, 'accountent_home.html')

def client_home(request):
    return render(request, 'client_home.html')

def client_menu(request):
    return render(request, 'client_menu.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def forgotpass(request):
    if request.method == "POST":
        uname = request.POST.get('t1', '')
        user = login.objects.filter(username=uname).count()
        if user >= 1:
            userlog = login.objects.filter(username=uname).values()
            for u in userlog:
                upass = u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('caclient20@gmail.com', 'szjxhpeezrpxeiek')
                mail.sendmail('caclient20@gmail.com', uname, content)
                mail.close()
                #messages.success(request, 'Your password has been sent to your email')
                return render(request, 'login.html')
        else:
            #messages.error(request, 'Enter registerd email only')
            return render(request, 'forgotpassword.html')
    return render(request, 'forgotpassword.html')


def insertlog(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        type="ca"
        login.objects.create(username=username, password=password,type=type)

    return render(request, 'insertlog.html')