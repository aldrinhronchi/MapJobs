
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User as use
from .models import User, PrestadorServico, Avaliacao, Qualificacao, FormsPayment, Cities, States, TypeService
from .forms import UserForm, PrestadorForm, AvaliacaoForm, QualificacaoForm, payForm, estForm, cityForm, activeForm


class CreateUser(CreateView):
    template_name = 'profile_cadastro.html'
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

    prestador = PrestadorServico.objects.all()

    return render(request, 'prestador_resultado.html', {'prest': prestador})



@login_required
def perfil(request):
    persons = get_object_or_404(User, pk=8)

    return render(request, 'profile.html', {'users': persons})


@login_required
def details(request, id):
    persons = get_object_or_404(PrestadorServico, pk=id)

    return render(request, 'prestador_details.html', {'users': persons})



@login_required
def pay_update(request, id):
    person = get_object_or_404(FormsPayment, pk=id)
    form = payForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('pay_lists')
    return render(request, 'payments_form.html', {'form': form})

@login_required
def pay_list(request):
    pays = FormsPayment.objects.all()

    return render(request, 'payments.html', {'pay': pays})


@login_required
def pay_new(request):
    form = payForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pay_lists')
    return render(request, 'payments_form.html', {'form': form})

@login_required
def pay_delete(request, id):
    pgto = get_object_or_404(FormsPayment, pk=id)
    form = payForm(request.POST or None, request.FILES or None, instance=pgto)
    if request.method == 'POST':
        pgto.delete()
        return redirect('pay_lists')
    return render(request, 'payments_delete_confirm.html', {'pay': pgto})

@login_required
def est_update(request, id):
    person = get_object_or_404(States, pk=id)
    form = estForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('est_lists')
    return render(request, 'est_form.html', {'form': form})

@login_required
def est_list(request):
    pays = States.objects.all()

    return render(request, 'est.html', {'est': pays})


@login_required
def est_new(request):
    form = estForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('est_lists')
    return render(request, 'est_form.html', {'form': form})

@login_required
def est_delete(request, id):
    pgto = get_object_or_404(States, pk=id)
    form = estForm(request.POST or None, request.FILES or None, instance=pgto)
    if request.method == 'POST':
        pgto.delete()
        return redirect('est_lists')
    return render(request, 'est_delete_confirm.html', {'est': pgto})


@login_required
def city_update(request, id):
    person = get_object_or_404(Cities, pk=id)
    form = cityForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('city_lists')
    return render(request, 'city_form.html', {'form': form})

@login_required
def city_list(request):
    pays = Cities.objects.all()

    return render(request, 'city.html', {'city': pays})


@login_required
def city_new(request):
    form = cityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('city_lists')
    return render(request, 'city_form.html', {'form': form})

@login_required
def city_delete(request, id):
    pgto = get_object_or_404(Cities, pk=id)
    form = cityForm(request.POST or None, request.FILES or None, instance=pgto)
    if request.method == 'POST':
        pgto.delete()
        return redirect('city_lists')
    return render(request, 'city_delete_confirm.html', {'city': pgto})


@login_required
def active_update(request, id):
    person = get_object_or_404(TypeService, pk=id)
    form = activeForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('active_lists')
    return render(request, 'active_form.html', {'form': form})

@login_required
def active_list(request):
    pays = TypeService.objects.all()

    return render(request, 'active.html', {'active': pays})


@login_required
def active_new(request):
    form = activeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('active_lists')
    return render(request, 'active_form.html', {'form': form})

@login_required
def active_delete(request, id):
    pgto = get_object_or_404(TypeService, pk=id)
    form = activeForm(request.POST or None, request.FILES or None, instance=pgto)
    if request.method == 'POST':
        pgto.delete()
        return redirect('active_lists')
    return render(request, 'active_delete_confirm.html', {'active': pgto})









@login_required
def auxs(request):

    return render(request,'auxiliar.html')





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
