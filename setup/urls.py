from django.contrib import admin
from django.urls import path, include
from crm.views import home

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')), # inclui as URLs do app CRM 
]
