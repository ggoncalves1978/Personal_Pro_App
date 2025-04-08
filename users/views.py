from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Empresa, CustomUser
from .forms import EmpresaForm, CustomUserForm

User = get_user_model()

# def criar_conta(request):
#     if request.method == "POST":
#         nome = request.POST.get("nome")
#         email = request.POST.get("email")
#         senha = request.POST.get("senha")

#         if User.objects.filter(username=email).exists():
#             messages.error(request, "Este e-mail já está cadastrado.")
#         else:
#             user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
#             login(request, user)
#             return redirect("dashboard")  # Redireciona para o dashboard após login

#     return render(request, "users/cadastro_empresa.html")


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")  # Redireciona para o painel da empresa
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_empresa(request):
    if request.method == "POST":
        empresa_form = EmpresaForm(request.POST)
        user_form = CustomUserForm(request.POST)

        if empresa_form.is_valid() and user_form.is_valid():
            empresa = empresa_form.save()

            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["senha"])  # Criptografar senha
            user.empresa = empresa  # Relacionar empresa ao usuário
            user.save()

            login(request, user)
            return redirect("dashboard")  # Redireciona para o dashboard

        else:
            messages.error(request, "Erro no cadastro. Verifique os dados.")

    else:
        empresa_form = EmpresaForm()
        user_form = CustomUserForm()

    return render(request, "users/cadastro_empresa.html", {"empresa_form": empresa_form, "user_form": user_form})