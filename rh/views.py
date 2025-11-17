from django.shortcuts import redirect, render
from .models import Funcionarios, Produto
from .forms import ContatoModelForm
from .models import Cliente
from django.contrib.auth import login
from .forms import RegistroForm

# Página inicial
def home(request):
    return render(request, 'home.html')

# Página de clientes
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

# Página de funcionários
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request, 'funcionarios.html', context)

# Formulário de contato
def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    else:
        form = ContatoModelForm()
    
    return render(request, 'contato/contatos.html', {'form': form})

# Página de sucesso do contato
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')

# Lista de produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    # Corrigido: caminho direto para o template, sem subpasta 'produtos'
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroForm()

    return render(request, 'registrar.html', {'form': form})