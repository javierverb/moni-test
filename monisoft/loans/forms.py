# -*- coding: utf-8 -*-
from django import forms

from loans.models import RequestLoan


class RequestLoanForm(forms.ModelForm):

    class Meta:
        model = RequestLoan
        fields = '__all__'
