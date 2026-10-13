import unittest
from unittest.mock import Mock
from aula189.app.regraEx1 import eh_email_valido, calcular_frete


class TestEmailValido(unittest.TestCase):
    def test_eh_email_valido_true(self):
        self.assertTrue(eh_email_valido('alex@alex.com'))
    def test_eh_email_valido_false_semarroba(self):
        self.assertFalse(eh_email_valido('alex.com'))
    def test_eh_email_valido_false_semponto(self):
        self.assertFalse(eh_email_valido('alex@com'))
    def test_eh_email_valido_false_comespacoinicio(self):
        self.assertFalse(eh_email_valido(' alex@alex.com'))
    def test_eh_email_valido_false_comespacofim(self):
        self.assertFalse(eh_email_valido('aax@alex.com '))


fake = Mock(return_value=0)

class TestCalcularFrete(unittest.TestCase):
    def test_calcular_frete_sepeso1(self):
        assert calcular_frete(0.1,'sp',fake) == 10.2
    def test_calcular_frete_sepeso2(self):
        assert calcular_frete(1,'sp',fake) == 12
    def test_calcular_frete_sepeso3(self):
        assert calcular_frete(10,'sp',fake) == 30
    def test_calcular_frete_erro1(self):
        with self.assertRaises(ValueError):
            calcular_frete(0,'sp',fake)
    def test_calcular_frete_erro2(self):
        with self.assertRaises(ValueError):
            calcular_frete(-1,'sp',fake)