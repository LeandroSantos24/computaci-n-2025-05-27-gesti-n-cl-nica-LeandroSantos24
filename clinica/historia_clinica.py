class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.entradas = []

    def agregar_entrada(self, entrada):
        self.entradas.append(entrada)
