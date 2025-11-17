from django.urls import path
from . import views

urlpatterns = [
    # Página inicial do app RH
    path('', views.home, name='home'),

    # Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),

    # Clientes
    path('clientes/', views.clientes, name='clientes'),

    # Funcionários
    path('funcionarios/', views.funcionarios, name='funcionarios'),

    # Formulário de contato
    path('contato/', views.formulario_contato_view, name='contatos'),

    # Página de sucesso após envio do formulário
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),

    path('registrar/', views.registrar, name='registrar'),

]
