import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from .forms import crm_form
from .models import crm


def home(request):
    return render(request, 'crm/home.html')

def criar_registro(request):
    if request.method == "POST":
        form = crm_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_clientes") # REdireciona após salvar
    else:
        form = crm_form()
    
    return render (request, "crm/formulario.html", {"form": form})

def listar_clientes(request):
    clientes = crm.objects.all()
    return render(request, "crm/lista_clientes.html", {"clientes": clientes})

def editar_registro(request, id):
    cliente = get_object_or_404(crm, id=id)
    if request.method == "POST":
        form = crm_form(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = crm_form(instance=cliente)
    
    return render(request, 'crm/editar_registro.html', {'form':form})

def excluir_registro(request, id):
    cliente = get_object_or_404(crm, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('lista_clientes')
    
    return render(request, 'crm/excluir_registro.html', {'cliente': cliente})

def importar_clientes(request):
    
    if request.method == "POST":
        arquivo = request.FILES.get("arquivo_excel")

        if not arquivo:
                       
            messages.error(request, "Por favor, selecione um arquivo.")
            return redirect("lista_clientes")
        
        
        try:
            df = pd.read_excel(arquivo)

            df['dia_da_semana'] = df['dia_da_semana'].astype('str')
            df['valor'] = df['valor'].astype('float')
            df['observacao'] = df['observacao'].astype('str')

            colunas_esperadas = [
                "nome", "telefone", "pais", "data_do_contato", "dia_da_semana", "canal",
                "data_de_fechamento", "follow_up", "chegou_na_oferta", "plano_escolhido",
                "valor", "observacao"
            ]

            print(f"📋 Colunas do DataFrame: {df.columns.tolist()}")  # 🔎 Debug


            if not all(col in df.columns for col in colunas_esperadas):
                messages.error(request, "Formato inválido. Verifique as colunas do arquivo.")
                return redirect("lista_clientes")

            with transaction.atomic():
                
                for _, row in df.iterrows():
                    print(f"Inserindo cliente: {row['nome']} - {row['telefone']}")  # 👀 Debug

                    cliente = crm.objects.create(
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

                    print(f"✅ Cliente {cliente.nome} salvo com sucesso!")  # 🔥 Confirmação

            messages.success(request, "Cliente(s) importado(s) com sucesso!")
            return redirect("lista_clientes")

        except Exception as e:
            
            messages.error(request, f"Erro ao importar: {str(e)}")
            return redirect("lista_clientes")

    return redirect("lista_clientes")