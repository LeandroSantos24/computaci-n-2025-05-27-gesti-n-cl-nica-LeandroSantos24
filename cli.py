from clinica.paciente import Paciente
from clinica.medico import Medico
from clinica.turno import Turno
from clinica.receta import Receta
from clinica.historia_clinica import HistoriaClinica
from clinica.clinica import Clinica

def menu():
    clinica = Clinica()
    while True:
        print("\n--- Sistema de Gestión Clínica ---")
        print("1. Agregar paciente")
        print("2. Agregar médico")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            paciente = Paciente(nombre, apellido, dni)
            clinica.agregar_paciente(paciente)
            print("Paciente agregado con éxito.")
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            especialidad = input("Especialidad: ")
            medico = Medico(nombre, apellido, especialidad)
            clinica.agregar_medico(medico)
            print("Médico agregado con éxito.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
