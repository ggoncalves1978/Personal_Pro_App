from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import cadastro_empresa, login_view, logout_view

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cadastro_empresa/", cadastro_empresa, name="cadastro_empresa"),
    # path("criar_conta/", criar_conta, name="criar_conta"),
]

