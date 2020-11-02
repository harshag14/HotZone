from django import forms
from .models import Virus
from django.db import models


def getviruslist():
    v=Virus.objects.all()
    #print(v)
    VIRUSES=[]
    for virus in v:
        temp=(virus.name , virus.name)
        VIRUSES.append(temp)
    return VIRUSES


class AddCaseDetailsForm(forms.Form):
    caseid = forms.IntegerField(label="Case ID")
    name = forms.CharField(label="Name   ", max_length=80)
    dateofbirth = forms.DateField(label="Date of Birth  ", widget=forms.SelectDateWidget(years=list(range(2020,1899,-1))))
    idnumber = forms.CharField(label="Identity Document Number  ", max_length=12)
    casetype = forms.CharField(label="Case Type  ", max_length=8, widget=forms.Select(choices=[("Local","Local"), ("Imported","Imported")]))
    dateconfirmed = forms.DateField(label="Date Confirmed  ", widget=forms.SelectDateWidget(years=list(range(2020,1899,-1))))
    virusname = forms.CharField(label="Virus Name  ", max_length=30, widget=forms.Select(choices=getviruslist()))


class AddLocationDetailsForm(forms.Form):
    caseid = forms.IntegerField(label="Case ID  ")
    place = forms.CharField(label="Location   ", max_length=80)
    datefrom = forms.DateField(label="Date From  ", widget=forms.SelectDateWidget(years=list(range(2020,1899,-1))))
    dateto = forms.DateField(label="Date To  ", widget=forms.SelectDateWidget(years=list(range(2020,1899,-1))))
    category = forms.CharField(label="Category  ", max_length=20)

