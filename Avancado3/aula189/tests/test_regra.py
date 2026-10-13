import unittest
from aula189.app.regra import normalizar_nome


class TestRegrasBasicas(unittest.TestCase):
    def test_normalizar_nome_remove_espacos_e_formata(self):
        self.assertEqual(normalizar_nome("  maria   da  silva "), "Maria Da Silva")


if __name__ == "__main__":
    unittest.main()