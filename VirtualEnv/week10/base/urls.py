from django.urls import path
#import views from current base app folder
from . import views

urlpatterns = [
    #Add path to route to base page view function
    path("base", views.base),
    
    path("contact", views.contact, name="contact")
]

