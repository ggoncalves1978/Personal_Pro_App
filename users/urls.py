from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import cadastro_empresa

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro_empresa/", cadastro_empresa, name="cadastro_empresa"),
]

