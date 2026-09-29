from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Propriedade(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="propriedades",
    )
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.cliente.nome}"


class Profissional(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    STATUS_CHOICES = [
        ("agendado", "Agendado"),
        ("em_andamento", "Em andamento"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        related_name="servicos",
    )
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="servicos",
    )
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="agendado",
    )
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.propriedade.nome} - {self.data}"
