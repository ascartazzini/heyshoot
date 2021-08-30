from datetime import datetime
from django.test import TestCase
from rh.models import Colaborador, Folguinha


class FeriasParaColaboradorTestCase(TestCase):

    def setUp(self):
        self.colaborador = Colaborador.objects.create(
            nome="Artur Scartazzini",
            cpf="134.882.575-84",  # Gerado aleatóriamente
            entrounashoot=datetime(2020, 1, 1).date()
        )

    def test_numero_dias_2020(self):
        """Testa o número de dias disponíveis para 2020."""
        self.assertEqual(self.colaborador.get_numero_dias_ferias_disponiveis(), 30)

    def test_colaborador_tirou_10_dias_ferias(self):
        """Testa se o colaborador tirou 10 dias de férias."""
        Folguinha.objects.create(
            quem=self.colaborador,
            inicio=datetime(2021, 2, 1).date(),
            fim=datetime(2021, 2, 10).date()
        )
        self.assertEqual(self.colaborador.get_numero_dias_ferias_disponiveis(), 20)
