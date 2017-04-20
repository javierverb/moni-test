# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from loans import views

urlpatterns = [
    url(r'^loan/$', views.request_loan, name="request-loan"),

    url(r'^request-loans/list/$',
        staff_member_required(views.AdministratorList.as_view()),
        name="request-loan-list"),

    url(r'^request-loans/(?P<pk>\d+)/update/$',
        staff_member_required(views.AdministratorUpdate.as_view()),
        name="request-loan-update"),

    url(r'^request-loans/(?P<pk>\d+)/delete/$',
        staff_member_required(views.AdministratorDelete.as_view()),
        name="request-loan-delete"),
]
