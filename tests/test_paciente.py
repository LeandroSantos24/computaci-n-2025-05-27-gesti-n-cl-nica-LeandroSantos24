import unittest
from clinica.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion(self):
        paciente = Paciente("Juan", "Pérez", "12345678")
        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.dni, "12345678")

if __name__ == '__main__':
    unittest.main()
