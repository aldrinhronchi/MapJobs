from django.forms import ModelForm
from .models import User, PrestadorServico, Avaliacao, Qualificacao, FormsPayment, Cities, States, TypeService


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','password','wats','photo','active']


class PrestadorForm(ModelForm):
    class Meta:
        model = PrestadorServico
        fields = ['person', 'cpf','cnpj','descricao','tipoServicos','atuacaoCidade','atuacaoEstado','formaPagamento', 'outroTelefone', 'redesSociais', 'statusConta']


class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['pessoa', 'prestador', 'qualidade', 'preco', 'comentarios','ip']


class payForm(ModelForm):
    class Meta:
        model = FormsPayment
        fields = ['nome']

class estForm(ModelForm):
    class Meta:
        model = States
        fields = ['state']

class cityForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['city']

class activeForm(ModelForm):
    class Meta:
        model = TypeService
        fields = ['description']



class QualificacaoForm(ModelForm):
    class Meta:
        model = Qualificacao
        fields = ['prestador','nome_curso','local','ano','certificado']






