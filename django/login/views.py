from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def contactanos_page(request):
    return render(request, 'contactanos.html')
