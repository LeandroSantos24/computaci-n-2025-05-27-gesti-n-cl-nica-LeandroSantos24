class Clinica:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.turnos = []
        self.historias_clinicas = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def asignar_turno(self, turno):
        self.turnos.append(turno)
