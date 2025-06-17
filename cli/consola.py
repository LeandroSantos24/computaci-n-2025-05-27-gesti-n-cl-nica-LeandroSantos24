from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno

def iniciar_consola():
    pacientes = []
    medicos = []

    while True:
        print("\n1. Agregar paciente\n2. Agregar médico\n3. Listar pacientes\n4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            dni = input("DNI del paciente: ")
            pacientes.append(Paciente(nombre, dni))
            print("Paciente agregado.")
        elif opcion == "2":
            nombre = input("Nombre del médico: ")
            especialidad = input("Especialidad: ")
            medicos.append(Medico(nombre, especialidad))
            print("Médico agregado.")
        elif opcion == "3":
            for p in pacientes:
                print(p)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
