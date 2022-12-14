from urllib import request
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def landing(request):
    return render(request, 'landing.html')

def apikeys(request):
    return render(request, 'account/api-keys.html')

def billing(request):
    return render(request, 'account/billing.html')

def logs(request):
    return render(request, 'account/logs.html')

def overview(request):
    return render(request, 'account/overview.html')

def referrals(request):
    return render(request, 'account/referrals.html')

def security(request):
    return render(request, 'account/security.html')

def settings(request):
    return render(request, 'account/settings.html')

def statements(request):
    return render(request, 'account/statements.html')
