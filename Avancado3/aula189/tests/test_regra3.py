import unittest
from unittest.mock import Mock
from aula189.app.regra3 import obter_cidade_por_cep


class TestCEP(unittest.TestCase):
    def test_obter_cidade_sem_chamar_servico_real(self):
        consulta_fake = Mock(return_value={"cidade": "Votorantim", "uf": "SP"})

        cidade = obter_cidade_por_cep("18110-000", consulta_fake)

        self.assertEqual(cidade, "Votorantim")
        consulta_fake.assert_called_once_with("18110-000")