# core/models.py
from django.db import models

class Funcionario(models.Model):
    # O Django cria um 'id' automático, mas como você tinha 'Matrícula',
    # vamos usar um AutoField que faz a mesma coisa: cria um número
    # novo e sequencial para cada funcionário.
    matricula = models.AutoField(primary_key=True)
    
    # Seus campos: Nome, Idade, Sexo
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20) # Ex: 'Masculino', 'Feminino'

    # Isso é só para o painel de admin do Django
    # mostrar o nome do funcionário, em vez de "Funcionario object (1)"
    def __str__(self):
        return f"{self.matricula}: {self.nome}"

class Alimento(models.Model):
    # O AutoField vai replicar sua lógica de 'novo_id'
    id = models.AutoField(primary_key=True)
    
    # Seus campos: nome, unidade, peso
    nome = models.CharField(max_length=100)
    unidade = models.FloatField() # Ex: 1.5 (para 1.5kg, 1.5L)
    peso = models.FloatField() # Ex: 0.5 (para 500g)

    # === MELHORIA IMPORTANTE ===
    # Notei que você pedia "valor" e "estoque" no seu input,
    # mas eles não estavam no seu dicionário 'novo_alimento' no Colab.
    # Adicionei eles aqui, pois eles são parte do seu modelo!
    
    # Para dinheiro (valor), NUNCA use FloatField. A melhor prática
    # é usar DecimalField para evitar erros de arredondamento.
    valor = models.DecimalField(max_digits=10, decimal_places=2) # Ex: 19.99
    
    estoque = models.IntegerField(default=0) # Quantidade em estoque

    def __str__(self):
        return self.nome