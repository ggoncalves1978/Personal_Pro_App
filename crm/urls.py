from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.criar_registro, name="novo_cliente"),
    path("lista/", views.listar_clientes, name="lista_clientes"),
    path("editar/<int:id>/", views.editar_registro, name="editar_registro"),
    path("excluir/<int:id>/", views.excluir_registro, name="excluir_registro"),
    path("importar/", views.importar_clientes, name="importar_clientes"),
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path("empresas/", views.listar_empresas, name="lista_empresas"),
    #path("criar-conta/", views.criar_conta, name="criar_conta"),
]
