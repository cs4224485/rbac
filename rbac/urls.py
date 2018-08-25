"""rbac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from app01.views import views, customer,payment
urlpatterns = [
    path('admin/', admin.site.urls),

    path('add_user/', views.add_user),
    path('role/', views.role),
    path('login/', views.login),

    re_path(r'^customer/list/$', customer.customer_list),
    re_path(r'^customer/add/$', customer.customer_add),
    re_path(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit),
    re_path(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del),
    re_path(r'^customer/import/$', customer.customer_import),
    re_path(r'^customer/tpl/$', customer.customer_tpl),

    re_path(r'^payment/list/$', payment.payment_list),
    re_path(r'^payment/add/$', payment.payment_add),
    re_path(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    re_path(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),
]
