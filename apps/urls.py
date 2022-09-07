from django.urls import path
from . import views
import apps

urlpatterns = [
    path('index', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('apikeys', views.apikeys, name='api-keys'),
    path('billing', views.billing, name='billing'),
    path('logs', views.logs, name='logs'),
    path('overview', views.overview, name='overview'),
    path('referrals', views.referrals, name='referrals'),
    path('security', views.security, name='security'),
    path('settings', views.settings, name='settings'),
    path('statements', views.statements, name='statements')
]