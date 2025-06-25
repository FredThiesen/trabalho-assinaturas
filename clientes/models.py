from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
