
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.conf.urls import url
from . import views

from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


app_name = 'master'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customerapp/', views.customer, name='customerapp'),
    url(r'^DRIVER/$', views.driver, name='DRIVERapp'),
    url(r'^(?P<d_id>\d+)/$', views.drivers, name='DRIVER'),
    url(r'^(?P<r_id>\d+)/(?P<c_id>\d+)/(?P<d_id>\d+)$', views.DRIVERselect, name='DRIVERselect'),


    url(r'^customerF/', views.customerFun, name='customerF'),

]
