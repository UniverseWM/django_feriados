from django.test import TestCase


class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_esponse(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exto(self):
        self.assertContains(self.resp, 'Natal')


class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')

    def test_200_esponse(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exto(self):
        self.assertContains(self.resp, 'Tiradentes')
