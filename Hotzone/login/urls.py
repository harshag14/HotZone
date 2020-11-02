from django.urls import path
from .views import loginView

urlpatterns = [
    path('', loginView , name="login_page")
]