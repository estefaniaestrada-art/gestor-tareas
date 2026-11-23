from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

APP = Path(__file__).resolve().parents[1] / "tareas.py"

class Interfaz(unittest.TestCase):
    def setUp(self):
        carpeta = self.enterContext(tempfile.TemporaryDirectory())
        self.archivo = Path(carpeta) / "tareas.json"

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(APP), "--archivo", str(self.archivo), *args],
            capture_output=True, text=True,
        )

    def test_alta_y_listado_persistente(self):
        self.assertEqual(self.cli("agregar", "  Estudiar  ").returncode, 0)
        listado = self.cli("listar")
        self.assertEqual(listado.returncode, 0)
        self.assertEqual(listado.stdout, "[pendiente] Estudiar\n")

    def test_rechaza_titulo_vacio(self):
        salida = self.cli("agregar", "  ")
        self.assertEqual(salida.returncode, 2)
        self.assertIn("El título es obligatorio", salida.stderr)
        self.assertFalse(self.archivo.exists())

    def test_lista_vacia(self):
        salida = self.cli("listar")
        self.assertEqual(salida.returncode, 0)
        self.assertEqual(salida.stdout, "")
