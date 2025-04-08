import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import crm_form, empresaForm
from .models import crm
from users.models import Empresa


def home(request):
    clientes = crm.objects.filter(empresa=request.user.empresa).order_by("-id")[:5] if request.user.is_authenticated else []
    return render(request, 'crm/home.html', {"clientes": clientes})


#@login_required
def criar_registro(request):
    if request.method == "POST":
        form = crm_form(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.empresa = request.user.empresa  # Associa a empresa do usuário logado
            cliente.save()
            messages.success(request, "Registro criado com sucesso!")
            return redirect("lista_clientes")
    else:
        form = crm_form()
    
    return render(request, "crm/formulario.html", {"form": form})

#@login_required
def listar_clientes(request):
    clientes = crm.objects.filter(empresa=request.user.empresa)  # Filtra por empresa
    return render(request, "crm/lista_clientes.html", {"clientes": clientes})

#@login_required
def editar_registro(request, id):
    cliente = get_object_or_404(crm, id=id, empresa=request.user.empresa)  # Garante acesso restrito à empresa

    if request.method == "POST":
        form = crm_form(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro atualizado com sucesso!")
            return redirect('lista_clientes')
    else:
        form = crm_form(instance=cliente)
    
    return render(request, 'crm/editar_registro.html', {'form': form})

#@login_required
def excluir_registro(request, id):
    cliente = get_object_or_404(crm, id=id, empresa=request.user.empresa)  # Garante que só exclui da empresa correta

    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Registro excluído com sucesso!")
        return redirect('lista_clientes')
    
    return render(request, 'crm/excluir_registro.html', {'cliente': cliente})

#@login_required
def importar_clientes(request):
    if request.method == "POST":
        arquivo = request.FILES.get("arquivo_excel")

        if not arquivo:
            messages.error(request, "Por favor, selecione um arquivo.")
            return redirect("lista_clientes")

        try:
            df = pd.read_excel(arquivo)

            df['dia_da_semana'] = df['dia_da_semana'].astype(str)
            df['valor'] = df['valor'].astype(float)
            df['observacao'] = df['observacao'].astype(str)

            colunas_esperadas = [
                "nome", "telefone", "pais", "data_do_contato", "dia_da_semana", "canal",
                "data_de_fechamento", "follow_up", "chegou_na_oferta", "plano_escolhido",
                "valor", "observacao"
            ]

            if not all(col in df.columns for col in colunas_esperadas):
                messages.error(request, "Formato inválido. Verifique as colunas do arquivo.")
                return redirect("lista_clientes")

            with transaction.atomic():
                for _, row in df.iterrows():
                    crm.objects.create(
                        empresa=request.user.empresa,  # Associa os clientes à empresa do usuário logado
                        nome=row["nome"],
                        telefone=row["telefone"],
                        pais=row["pais"],
                        data_do_contato=row["data_do_contato"],
                        dia_da_semana=row["dia_da_semana"],
                        canal=row["canal"],
                        data_de_fechamento=row["data_de_fechamento"],
                        follow_up=row["follow_up"],
                        chegou_na_oferta=row["chegou_na_oferta"],
                        plano_escolhido=row["plano_escolhido"],
                        valor=row["valor"],
                        observacao=row["observacao"] if pd.notna(row["observacao"]) else ""
                    )

            messages.success(request, "Cliente(s) importado(s) com sucesso!")
            return redirect("lista_clientes")

        except Exception as e:
            messages.error(request, f"Erro ao importar: {str(e)}")
            return redirect("lista_clientes")

    return redirect("home")


#@login_required
def cadastrar_empresa(request):
    if request.method == "POST":
        form = empresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empresa cadastrada com sucesso!")
            return redirect("lista_empresas")
    else:
        form = empresaForm()
    
    return render(request, "crm/cadastrar_empresa.html", {"form": form})

#@login_required
def listar_empresas(request):
    empresas = empresa.objects.all()
    return render(request, 'crm/lista_empresas.html', {'empresas': empresas})