from django.db import models

# Create your models here.
class login(models.Model):
       username = models.CharField(max_length=200)
       password = models.CharField(max_length=50)
       type = models.CharField(max_length=50)


class userregistration(models.Model):
       username= models.CharField(max_length=200)
       password= models.CharField(max_length=200)
       email = models.CharField(max_length=200)
       mobilenumber= models.CharField(max_length=200)

class client_details(models.Model):
       client_id = models.CharField(max_length=200)
       client_name = models.CharField(max_length=200)
       pan = models.CharField(max_length=200)
       mobile = models.CharField(max_length=200)
       email_id = models.CharField(max_length=200)
       address = models.CharField(max_length=200)
       aadhar_no = models.CharField(max_length=200)
       start_date = models.CharField(max_length=200)


class account_details(models.Model):
    client_id = models.CharField(max_length=200)
    account_no = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=200)


class firm_details(models.Model):
       firm_id = models.CharField(max_length=200)
       firm_name = models.CharField(max_length=200)
       client_id= models.CharField(max_length=200)
       website = models.CharField(max_length=200)
       address = models.CharField(max_length=200)
       cin = models.CharField(max_length=200)

class audit_types(models.Model):
        audit_id = models.CharField(max_length=200)
        audit_type = models.CharField(max_length=200)
        audit_month = models.CharField(max_length=200)
        start_date = models.CharField(max_length=200)
        end_date = models.CharField(max_length=200)
        fees = models.CharField(max_length=200)


class filing_date(models.Model):
    filing_id = models.CharField(max_length=200)
    filing_type = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

class client_type(models.Model):
    client_id = models.CharField(max_length=200)
    client_type = models.CharField(max_length=200)
    pan = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)


class intimation(models.Model):
    client_id = models.CharField(max_length=200)
    intimation_type = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    details = models.CharField(max_length=200)


class document_detail(models.Model):
    client_id = models.CharField(max_length=200)
    document_id = models.CharField(max_length=200)
    document_name = models.CharField(max_length=200)
    uplaod_date = models.CharField(max_length=200)
    url = models.FileField(upload_to='documents/')


class audit_request(models.Model):
    firm_id = models.CharField(max_length=200)
    request_id = models.CharField(max_length=200)
    audit_type = models.CharField(max_length=200)
    request_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class accountent(models.Model):
    accountet_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)

