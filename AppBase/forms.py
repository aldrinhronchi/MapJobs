from django.forms import ModelForm
from .models import User, PrestadorServico, Avaliacao, Qualificacao


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


class QualificacaoForm(ModelForm):
    class Meta:
        model = Qualificacao
        fields = ['prestador','nome_curso','local','ano','certificado']






