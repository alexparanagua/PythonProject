import unittest
from aula189.app.regra2 import calcular_desconto


class TestDesconto(unittest.TestCase):
    def test_aplica_cupom_quando_valor_minimo(self):
        self.assertEqual(calcular_desconto(100, "PROMO10"), 90.00)
        self.assertEqual(calcular_desconto(250, "PROMO10"), 225.00)

    def test_nao_aplica_cupom_abaixo_do_minimo(self):
        self.assertEqual(calcular_desconto(99.99, "PROMO10"), 99.99)

    def test_erro_para_valor_negativo(self):
        with self.assertRaises(ValueError):
            calcular_desconto(-1, "PROMO10")