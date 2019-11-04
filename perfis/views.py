from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



@login_required
def index(request):
    perfis = Perfil.objects.all()
    context = {
        'perfis' : Perfil.objects.all(),
        'perfil_logado' : get_perfil_logado(request)
    }
    return render(request, 'index.html', context)


@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    context = {
        'perfil' : perfil,
        'perfil_logado' : get_perfil_logado(request),
        'ja_eh_contato': ja_eh_contato
    }
    return render(request, 'perfil.html', context)


@permission_required('perfis.add_convite', raise_exception=False)
@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


def get_perfil_logado(request):
    return request.user.perfil
