import unittest
from modelo.medico import Medico

class TestMedico(unittest.TestCase):
    def test_creacion(self):
        m = Medico("Ana", "Cardiología")
        self.assertEqual(m.nombre, "Ana")
        self.assertEqual(m.especialidad, "Cardiología")
