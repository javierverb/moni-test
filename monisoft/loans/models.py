# -*- coding: utf-8 -*-
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True,
                                   null=True,
                                   blank=True)
    modified = models.DateTimeField(auto_now=True,
                                    null=True,
                                    blank=True)


class RequestLoan(TimeStampedModel):

    class Meta:
        verbose_name = "RequestLoan"
        verbose_name_plural = "RequestLoans"

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    LIST_VALIDATORS = [validators.MinValueValidator(1)]

    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)
    email = models.EmailField(_('email address'))
    document_number = models.CharField(_('dni'), max_length=40)

    request_amount = models.PositiveIntegerField(null=True,
                                                 validators=LIST_VALIDATORS,
                                                 default=1)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default='F')

    def __str__(self):
        return "Request maked by: {}".format(self.first_name)
