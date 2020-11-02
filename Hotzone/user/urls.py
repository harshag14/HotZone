from django.urls import path
from .views import userView, AddCaseDetails, AddLocationDetails, CaseDetailsAdded, LocationDetailsAdded

urlpatterns = [
    path('', userView , name="user_page"),
    path('addcasedetails/', AddCaseDetails.as_view(), name="add_case_details"),
    path('addlocationdetails/', AddLocationDetails.as_view(), name="add_location_details"),
    path('casedetailsadded/', CaseDetailsAdded.as_view(), name="case_details_added" ),
    path('locationdetailsadded/', LocationDetailsAdded.as_view(), name="location_details_added" )
]