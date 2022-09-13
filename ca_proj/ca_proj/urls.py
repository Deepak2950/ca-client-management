"""ca_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url

from ca_client import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('index',views.index,name='index'),
    url('login',views.login,name='login'),
    url('insertuserregistration',views.insertuserregistration,name='insertuserregistration'),
    url('insertclient_details',views.insertclient_details,name='insertclient_details'),
    url('logcheck',views.logcheck,name='logcheck'),
    url('insertaccount_details', views.insertaccount_details, name='insertaccount_details'),
    url('insertfirm_details', views.insertfirm_details, name='insertfirm_details'),
    url('insertaudit_type', views.insertaudit_type, name='insertaudit_type'),
    url('insertfiling_date', views.insertfiling_date, name='insertfiling_date'),
    url('insertclient_type', views.insertclient_type, name='insertclient_type'),
    url('insertintimation', views.insertintimation, name='insertintimation'),
    url('insertdocument_detail', views.insertdocument_detail, name='insertdocument_detail'),
    url('insertaudit_request', views.insertaudit_request, name='insertaudit_request'),

    url('insertaccountent', views.insertaccountent, name='insertaccountent'),
    url('insertlog', views.insertlog, name='insertlog'),


    url('viewdocdetails', views.viewdocdetails, name='viewdocdetails'),
    url('viewaccdetails', views.viewaccdetails, name='viewaccdetails'),
    url('viewauditrequest', views.viewauditrequest, name='viewauditrequest'),
    url('viewaudittypes', views.viewaudittypes, name='viewaudittypes'),
    url('viewclientdetails', views.viewclientdetails, name='viewclientdetails'),
    url('viewclienttypes', views.viewclienttypes, name='viewclienttypes'),
    url('viewfilingdate', views.viewfilingdate, name='viewfilingdate'),
    url('viewfirmdetails', views.viewfirmdetails, name='viewfirmdetails'),
    url('viewintimation', views.viewintimation, name='viewintimation'),
    url('viewuserregistration', views.viewuserregistration, name='viewuserregistration'),

    #delete code deleteuserregistration
     url('deleteuserregistration/(?P<pk>\d+)/$', views.deleteuserregistration, name='deleteuserregistration'),
     url('deleteaccdetails/(?P<pk>\d+)/$', views.deleteaccdetails, name='deleteaccdetails'),
     url('deleteauditrequest/(?P<pk>\d+)/$', views.deleteauditrequest, name='deleteauditrequest'),
     url('deleteaudittypes/(?P<pk>\d+)/$', views.deleteauditrequest, name='deleteaudittypes'),
     url('deleteclientdetails/(?P<pk>\d+)/$', views.deleteclientdetails, name='deleteclientdetails'),
     url('deleteclienttypes/(?P<pk>\d+)/$', views.deleteclienttypes, name='deleteclienttypes'),
     url('deletedocumentdetails/(?P<pk>\d+)/$', views.deletedocumentdetails, name='deletedocumentdetails'),
     url('deletefilingdate/(?P<pk>\d+)/$', views.deletefilingdate, name='deletefilingdate'),
     url('deletefirmdetails/(?P<pk>\d+)/$', views.deletefirmdetails, name='deletefirmdetails'),
     url('deleteintimation/(?P<pk>\d+)/$', views.deleteintimation, name='deleteintimation'),


    url('accountent_menu', views.accountent_menu, name='accountent_menu'),

    url('accountent_home', views.accountent_home, name='accountent_home'),

    url('client_home', views.client_home, name='client_home'),
    url('client_menu', views.client_menu, name='client_menu'),

    url('admin_home', views.admin_home, name='admin_home'),

    url('forgotpass', views.forgotpass, name='forgotpass'),





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
