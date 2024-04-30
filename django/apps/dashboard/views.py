from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return render(request, 'dashboard.html')