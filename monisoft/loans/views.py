# -*- coding: utf-8 -*-
import json
import urllib.request as urllib
from urllib.error import HTTPError

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import (ListView, UpdateView, DeleteView)

from loans.models import RequestLoan
from loans.forms import RequestLoanForm


def request_loan(request):
    if request.method == 'POST':
        form = RequestLoanForm(request.POST)
        if form.is_valid():
            form.save()
            url = 'http://scoringservice.moni.com.ar:7001/api/v1/scoring/'
            query_string = "?{}".format(request.POST.urlencode())
            req = urllib.Request(url + query_string)
            try:
                response = urllib.urlopen(req)
                data = response.read().decode('utf-8')
                json_data = json.loads(data)
                return JsonResponse({'status': '200', 'data': json_data})
            except HTTPError as e:
                return JsonResponse({'status': '500', 'data': ''})
        else:
            errors = form.errors
            return JsonResponse({'status': 'form_error', 'form_error': errors})
    else:
        form = RequestLoanForm()

    return render(request, 'loans/request-loan.html', {'form': form})


# se asume que un administrador de préstamos es parte del 'staff'
class AdministratorList(ListView):
    model = RequestLoan
    context_object_name = 'request_loans'
    template_name = 'administrator/dashboard-loans-list.html'


class AdministratorUpdate(UpdateView):
    model = RequestLoan
    fields = ['first_name', 'last_name', 'email', 'document_number',
              'request_amount', 'gender']
    context_object_name = 'request_loan'
    template_name = 'administrator/dashboard-loans-update.html'
    success_url = reverse_lazy('request-loan-list')


class AdministratorDelete(DeleteView):
    model = RequestLoan
    template_name = 'administrator/dashboard-loans-delete.html'
    success_url = reverse_lazy('request-loan-list')
