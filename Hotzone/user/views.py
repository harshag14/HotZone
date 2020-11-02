from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import Patient, Location, Case, Virus, CaseLocation
from django.views.generic.edit import FormView 
from .forms import AddCaseDetailsForm, AddLocationDetailsForm
import json
import urllib.request
from django.template import Template
from django.contrib import messages


class AddCaseDetails(FormView):
    template_name="casedetails.html"
    form_class=AddCaseDetailsForm
    success_url='/user/casedetailsadded/'

class AddLocationDetails(FormView):
    template_name="locationdetails.html"
    form_class=AddLocationDetailsForm
    success_url='/user/locationdetailsadded/'


class CaseDetailsAdded(View):
    def post(self, request):
        form = AddCaseDetailsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if(Case.objects.filter(case_id=data["caseid"]).exists()):
                return render(request, "error.html")
            patient, created = Patient.objects.get_or_create(
                idnumber = data["idnumber"], 
                defaults={
                    'name': data['name'],
                    'dateofbirth': data['dateofbirth']
                }
            )

            virus = Virus.objects.get(name=data["virusname"])
            #print(virus.maxinfectiousperiod)

            
            case, casecreated = Case.objects.get_or_create(
                case_id = data["caseid"],
                defaults={
                    'patient' : patient,
                    'virus' : virus,
                    'dateconfirmed' : data["dateconfirmed"],
                    'casetype' : data["casetype"]
                }
            )

            #print(type(patient))

            message = {
                "name": patient.name,
                "idnumber": patient.idnumber,
                "dateofbirth": patient.dateofbirth,
                "virusname": virus.name,
                "disease": virus.commonname,
                "caseid": case.case_id,
                "dateconfirmed": case.dateconfirmed,
                "casetype": case.casetype
            }
            print(message)
            return render(request, "casedetailsadded.html", message)

class LocationDetailsAdded(View):
    def post(self, request):
        form = AddLocationDetailsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            url = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q="
            query = data['place'].replace(' ', '%20')
            #print(query)
            geodata = json.loads(urllib.request.urlopen(url+query).read().decode())
            x=geodata[0]['x']
            y=geodata[0]['y']
            addr=geodata[0]['addressEN']
            #print(x,y,addr)

            #print(geodata)
    
            locationdata = Location.objects.create(
                place = data['place'],
                xcoord = x,
                ycoord = y,
                address = addr
            ) 
            
            caselocation = CaseLocation.objects.create(
                case=Case.objects.get(case_id=data['caseid']),
                location = locationdata,
                datefrom = data['datefrom'],
                dateto = data['dateto'],
                category = data['category']
            )

            message ={
                "caseid": caselocation.case.case_id,
                "patientname": str(caselocation.case.patient).lstrip('0123456789'),
                "location": locationdata.place,
                "address": locationdata.address,
                "xcoord": locationdata.xcoord,
                "ycoord": locationdata.ycoord,
                "datefrom": caselocation.datefrom,
                "dateto": caselocation.dateto,
                "category": caselocation.category
            }

            return render(request, "locationdetailsadded.html", message)
        

# Create your views here.
def userView(request):
    return render(request, "user.html")

