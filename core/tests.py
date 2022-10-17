from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime


class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_esponse(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exto(self):
        self.assertContains(self.resp, 'Natal')

    def test_templete(self):
        self.assertTemplateUsed(self.resp, 'natal.html')


class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')

    def test_200_esponse(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exto(self):
        self.assertContains(self.resp, 'Tiradentes')


class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado,
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)

    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)