from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e',
                      'em', 'a', 'o', 'as', 'os', 'para', 'com']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
