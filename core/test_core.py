from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from .models import Cliente, Propriedade, Profissional, Servico


class ModelTests(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Cliente Teste",
            email="cliente@example.com",
            telefone="6195550100",
        )

        self.propriedade = Propriedade.objects.create(
            cliente=self.cliente,
            nome="Ocean View Apt",
            endereco="123 Main St",
            cidade="San Diego",
        )

        self.profissional = Profissional.objects.create(
            nome="Ana Lima",
            email="ana@example.com",
            telefone="6195550200",
        )

        self.servico = Servico.objects.create(
            propriedade=self.propriedade,
            profissional=self.profissional,
            data=date(2026, 10, 14),
            horario=time(10, 0),
            status="agendado",
            observacoes="Serviço de teste",
        )

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Cliente Teste")

    def test_propriedade_str(self):
        self.assertEqual(
            str(self.propriedade),
            "Ocean View Apt - Cliente Teste",
        )

    def test_profissional_str(self):
        self.assertEqual(str(self.profissional), "Ana Lima")

    def test_servico_str(self):
        self.assertEqual(
            str(self.servico),
            "Ocean View Apt - 2026-10-14",
        )

    def test_status_padrao_servico(self):
        servico = Servico.objects.create(
            propriedade=self.propriedade,
            profissional=self.profissional,
            data=date(2026, 10, 15),
            horario=time(9, 0),
        )
        self.assertEqual(servico.status, "agendado")


class ViewTests(TestCase):

    def test_dashboard(self):
        response = self.client.get(reverse("core:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/dashboard.html")

    def test_novo_servico(self):
        response = self.client.get(reverse("core:novo_servico"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/novo_servico.html")

    def test_detalhe_servico(self):
        response = self.client.get(reverse("core:detalhe_servico"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/detalhe_servico.html")
