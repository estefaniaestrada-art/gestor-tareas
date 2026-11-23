import unittest
from tareas import registrar

class Registro(unittest.TestCase):
    def test_registra_titulo_limpio(self):
        self.assertEqual(
            registrar([], "  Estudiar  "),
            [{"titulo": "Estudiar", "hecha": False}],
        )
