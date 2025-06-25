from django.shortcuts import render, redirect, get_object_or_404
from .models import Assinatura
from .forms import AssinaturaForm
from clientes.models import Cliente
from django.contrib import messages
from django.views.decorators.http import require_POST

def nova_assinatura(request):
    if request.method == 'POST':
        form = AssinaturaForm(request.POST)
        if form.is_valid():
            assinatura = form.save()
            # Salva os clientes selecionados na ManyToMany
            assinatura.clientes.set(form.cleaned_data['clientes'])
            messages.success(request, 'Assinatura criada com sucesso!')
            return redirect('lista_assinaturas')
        else:
            messages.error(request, 'Erro ao criar assinatura. Verifique os dados.')
    else:
        form = AssinaturaForm()
    return render(request, 'assinaturas/nova_assinatura.html', {'form': form})

def lista_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas/lista_assinaturas.html', {'assinaturas': assinaturas})

def assinatura_por_clientes(request, id):
    assinatura = get_object_or_404(Assinatura, id=id)
    clientes = assinatura.clientes.all()
    sort = request.GET.get('sort')
    if sort == 'nome':
        clientes = clientes.order_by('nome')
    elif sort == 'cpf':
        clientes = clientes.order_by('cpf')
    elif sort == 'email':
        clientes = clientes.order_by('email')
        
    print(f"Sort: {sort}")
    print(f"Clientes: {clientes}")
    return render(request, 'assinaturas/assinatura_por_clientes.html', {'assinatura': assinatura, 'clientes': clientes, 'sort': sort})

@require_POST
def deletar_assinatura(request, id):
    assinatura = get_object_or_404(Assinatura, id=id)
    assinatura.delete()
    messages.success(request, 'Assinatura deletada com sucesso!')
    return redirect('lista_assinaturas')
