from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return HttpResponse("<h2>Base Page</h2>")

def contact(request):
    return(render(request, "contact.html"))

#Array 
def courses(request):
    print(coursesArray)
    return(render(
        request,
    ))