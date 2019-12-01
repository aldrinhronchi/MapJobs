from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30 ,  null=False, blank=False)
    user_novo = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=254, null=False, blank=False)
    wats = models.CharField(max_length=30, null=False, blank=False)
    photo = models.ImageField(upload_to='user_fotos', null=True, blank=True)
    dates = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

objetos = models.Manager()

class TypeService(models.Model):
    #prestador = models.ForeignKey(PrestadorServico, null=False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.description


class FormsPayment(models.Model):

    nome = models.CharField(max_length=30, null=False, blank=False)
    #icone = models.ImageField(upload_to='icones', null=False, blank=False)

    def __str__(self):
        return self.nome


class Cities(models.Model):

    city = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.city


class States(models.Model):
    state = models.CharField(max_length=50 ,null=False, blank=False)

    def __str__(self):
        return self.state


class PrestadorServico(models.Model):

    person = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=10, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    descricao = models.TextField()
    tipoServicos = models.ManyToManyField(TypeService)
    atuacaoCidade = models.ManyToManyField(Cities)
    atuacaoEstado = models.ManyToManyField(States)
    formaPagamento = models.ManyToManyField(FormsPayment)
    outroTelefone = models.CharField(max_length=29, null=True, blank=True)
    redesSociais = models.CharField(max_length=99, null=True, blank=True)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    statusConta = models.BooleanField(default=True)

    def __str__(self):
        return self.person.first_name

class Avaliacao(models.Model):
    pessoa = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    prestador = models.ForeignKey(PrestadorServico, null=False, blank=False, on_delete=models.CASCADE)
    qualidade = models.IntegerField(null=False, blank=False)
    preco = models.IntegerField(null=False, blank=False)
    comentarios = models.TextField()
    ip = models.GenericIPAddressField(null=False, blank=False)
    data_avaliacao = models.DateTimeField(auto_now=False, auto_now_add=True)


class Qualificacao(models.Model):
    prestador = models.ForeignKey(PrestadorServico, null=False, blank=False, on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=30, null=False, blank=False)
    local = models.CharField(max_length=30, null=False, blank=False)
    ano = models.CharField(max_length=4, null=False, blank=False)
    # file will be uploaded to MEDIA_ROOT/uploads
    certificado = models.FileField(upload_to='uploads', null=True, blank=True)




