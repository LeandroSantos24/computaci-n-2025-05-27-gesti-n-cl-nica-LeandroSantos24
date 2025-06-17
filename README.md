# Sistema de Gestión para Clínica 🏥

## Alumno
**Leandro Santos**  
Estudiante de Ingeniería en Sistemas, Universidad de Mendoza  

---

## 1. 🎯 Objetivo del Proyecto
Desarrollar un sistema en Python para gestionar una clínica, que permita:
- Registrar y gestionar **pacientes**.
- Dar de alta y organizar **médicos** con sus especialidades.
- Generar y asignar **turnos**, evitando conflictos de horario.
- Crear **historias clínicas** y registrar **recetas**.
- Crear una **interface de línea de comandos (CLI)** para interactuar con el sistema de manera sencilla.

---

## 2. 🛠️ Estructura y Requisitos Técnicos

### 2.1 Archivos y carpetas
```
clinica/
├── paciente.py
├── medico.py
├── turno.py
├── receta.py
├── especialidad.py
├── historia_clinica.py
├── clinica.py
└── cli.py

tests/
├── test_paciente.py
├── test_medico.py
├── test_turno.py
├── test_receta.py
├── test_especialidad.py
├── test_historia_clinica.py
└── test_clinica.py
README.md
.gitignore
```

### 2.2 Clases y validaciones
Cada clase implementa atributos propios y métodos para:
- Validaciones de datos (por ejemplo, formatos de DNI, fechas, horarios).
- Excepciones personalizadas para manejo de errores (por ejemplo, `TurnoYaReservadoError`, `PacienteNoEncontradoError`).
- Testeo completo de casos positivos y negativos usando `unittest`.

### 2.3 CLI
Archivo `cli.py` que permite:
- Registrar pacientes y médicos.
- Pedir turnos y consultarlos.
- Ver historias clínicas y recetar tratamientos.
- Opciones claras, menús interactivos y mensajes de validación de errores.

---

## 3. 📦 Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone git@github.com:um-computacion/computaci-n-2025-05-27-gesti-n-cl-nica-LeandroSantos24.git
   cd computaci-n-2025-05-27-gesti-n-cl-nica-LeandroSantos24
   ```

2. (Opcional) Crear un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instalar dependencias (si corresponde):
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```bash
   python cli.py
   ```

---

## 4. ✅ Cómo ejecutar los tests

Están organizados en la carpeta `tests/`. Usar `unittest`:

```bash
python -m unittest discover -v
```

O, si usás `pytest`:

```bash
pytest -q
```

Cada test verifica tanto casos correctos como errores esperados.

---

## 5. 🧩 Diseño e implementación

- Uso de **POO**: cada entidad clínica es una clase con responsabilidad clara.
- **Modularización**: lógica de negocio en `clinica.py`, CLI por separado.
- Manejo de **errores robusto** con excepciones personalizadas.
- **Alta cobertura de tests** asegurando funcionamiento confiable.

---

## 6. 📝 Documentación Adicional

- Dentro de cada archivo `.py` está la documentación de clases y métodos (docstrings).
- Las validaciones y excepciones están descriptas en `exceptions.py` y explicadas en tests.
- El README responde: quién soy, qué hace el sistema, cómo se usa y cómo se prueba.

---

## 7. 📚 Referencias

Plantilla provista por la cátedra de Computación I – Universidad de Mendoza  
