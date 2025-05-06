from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=300)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100)

class Genero(models.Model):
    nome_categoria = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, related_name='livros')
    ano = models.DateField()
    editora = models.ForeignKey(Editora, related_name='livros')
    genero = models.ForeignKey(Genero, related_name='livros')

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_registro = models.DateField(auto_now_add=True)

class Emprestimo(models.Model):
    livros = models.ManyToManyField(Livro, related_name='emprestimos')
    usuario = models.ForeignKey(Usuario, related_name='emprestimos')
    data_emprestimo = models.DateTimeField()

class Reserva(models.Model):
    livros = models.ManyToManyField(Livro, related_name='reservas')
    usuario = models.ForeignKey(Usuario, related_name='reservas')
    data_reserva = models.DateTimeField

class Multa(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='multas')
    valor = models.FloatField()
    data_pagamento = models.DateField()

