from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def contactanos_page(request):
    return render(request, 'contactanos.html')

def login_form(request):
    return render(request, 'login.html')
