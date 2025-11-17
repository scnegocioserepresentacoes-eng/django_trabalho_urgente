from django.db import models
from django.utils import timezone

# Create your models here.
class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome
    
    # contato/models.py

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    categoria = models.CharField(max_length=100, verbose_name="Categoria")
    descricao = models.TextField(verbose_name="Descrição do Produto")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Imagem do Produto")
    criado_em = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']  # Ordena pelo nome por padrão

    def __str__(self): 
        return self.nome


class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=20, blank=True, null=True)
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField()
    email = models.EmailField()
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']



