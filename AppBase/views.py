
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User as use
from .models import User, PrestadorServico, Avaliacao, Qualificacao
from .forms import UserForm, PrestadorForm, AvaliacaoForm, QualificacaoForm


class CreateUser(CreateView):
    template_name = 'cadastro.html'
    model = User()
    fields = '__all__'
    success_url = reverse_lazy("home")


class CriaPrestador(CreateView):
    template_name = 'prestadores.html'
    model = PrestadorServico()
    fields = '__all__'
    success_url = reverse_lazy("home")

# lista geral sem login
def prestador_list(request):
   # busca = pesquisa
    #if busca:

      #  prestador = PrestadorServico.objects.all()
       # prestador = PrestadorServico.objects.filter(PrestadorServico.tipoServicos==busca)
   # else:
    prestador = PrestadorServico.objects.all()


    return render(request, 'resultado.html', {'prest': prestador})



@login_required
def perfil(request):
    persons = get_object_or_404(User, pk=8)

    return render(request, 'profile.html', {'users': persons})


@login_required
def details(request, id):
    persons = get_object_or_404(PrestadorServico, pk=id)

    return render(request, 'details.html', {'users': persons})



@login_required
def user_update(request, id):
    person = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_form.html', {'form': form})



@login_required
def prestador_new(request):
    form = PrestadorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'prestador_form.html', {'form': form})


@login_required
def prestador_update(request, id):
    person = get_object_or_404(PrestadorServico, pk=id)
    form = PrestadorForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('prestador_list')
    return render(request, 'prestador_form.html', {'form': form})


@login_required
def prestador_delete(request, id):
    person = get_object_or_404(PrestadorServico, pk=id)
    form = PrestadorForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('prestador_list')
    return render(request, 'prestador_delete_confirm.html', {'prestador': person})


# Avaliação dos prestadores de serviço

@login_required
def avaliacao_list(request):
    aval = Avaliacao.objects.all()
    return render(request, 'avaliacao.html', {'avaliacao': aval})


@login_required
def avaliacao_new(request):
    form = AvaliacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('avaliacao_list')
    return render(request, 'avaliacao_form.html', {'form': form})


@login_required
def avaliacao_update(request, id):
    avalicao = get_object_or_404(Avaliacao, pk=id)
    form = AvaliacaoForm(request.POST or None, request.FILES or None, instance=avalicao)
    if form.is_valid():
        form.save()
        return redirect('avaliacao_list')
    return render(request, 'avaliacao_form.html', {'form': form})


@login_required
def avaliacao_delete(request, id):
    avaliacao = get_object_or_404(Avaliacao, pk=id)
    form = AvaliacaoForm(request.POST or None, request.FILES or None, instance=avaliacao)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('avaliacao_list')
    return render(request, 'avaliacao_delete_confirm.html', {'avaliacao': avaliacao})


# Qualificação dos prestadores de serviço

@login_required
def qualificacao_list(request):
    qual = Qualificacao.objects.all()
    return render(request, 'qualificacao.html', {'qualificacao': qual})


@login_required
def qualificacao_new(request):
    form = QualificacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('qualificacao_list')
    return render(request, 'qualificacao_form.html', {'form': form})


@login_required
def qualificacao_update(request, id):
    qualific = get_object_or_404(Qualificacao, pk=id)
    form = QualificacaoForm(request.POST or None, request.FILES or None, instance=qualific)
    if form.is_valid():
        form.save()
        return redirect('qualificacao_list')
    return render(request, 'qualificacao_form.html', {'form': form})


@login_required
def qualificacao_delete(request, id):
    qualific = get_object_or_404(Qualificacao, pk=id)
    form = QualificacaoForm(request.POST or None, request.FILES or None, instance=qualific)
    if request.method == 'POST':
        qualific.delete()
        return redirect('qualificacao_list')
    return render(request, 'qualificacao_delete_confirm.html', {'qualificacao': qualific})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
