from django.contrib import admin
from django.urls import path, include
from crm.views import home   # Importar a view da home

urlpatterns = [
    path("", home, name="home"),  # Home sem login
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')), # inclui as URLs do app CRM 
    path('users/', include("users.urls")), # Adiciona as URLs do users
    path("accounts/", include("django.contrib.auth.urls")), # Adiciona as URLs de login/logout
    path("accounts/", include("users.urls")),  # Inclui as URLs do app users
]
