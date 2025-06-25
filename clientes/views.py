from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from assinaturas.models import Assinatura
from django.contrib import messages

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('lista_clientes')
        else:
            messages.error(request, 'Erro ao cadastrar cliente. Verifique os dados.')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro_clientes.html', {'form': form})

def lista_clientes(request):
    query = request.GET.get('q', '')
    if query:
        clientes = Cliente.objects.filter(nome__icontains=query)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def cliente_assinaturas(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    assinaturas = Assinatura.objects.filter(clientes=cliente)
    return render(request, 'clientes/cliente_assinaturas.html', {'cliente': cliente, 'assinaturas': assinaturas})
