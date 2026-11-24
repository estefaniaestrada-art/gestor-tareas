# Gestor de tareas por consola

**Proyecto de Integración Continua**  
Estefanía Estrada Pérez  
Corporación Universitaria del Caribe (CECAR)

## 1. Descripción del proyecto

Gestor de tareas es una aplicación desarrollada en Python que permite registrar tareas pendientes y almacenarlas en un archivo JSON para consultarlas posteriormente.

El proyecto se desarrolló como caso práctico de integración continua, aplicando control de versiones con Git, desarrollo mediante ramas, pruebas automatizadas y GitHub Actions.

## 2. Requisitos

- Python 3.12 o superior.
- Git.
- Cuenta de GitHub para consultar el repositorio.

## 3. Ejecución de la aplicación

Desde la raíz del proyecto, se puede crear un entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Para registrar una tarea:

```bash
python tareas.py --archivo ejemplo.json agregar "Estudiar"
```

Para consultar las tareas:

```bash
python tareas.py --archivo ejemplo.json listar
```

La salida esperada para la tarea registrada es:

```text
[pendiente] Estudiar
```

Si no se especifica el parámetro `--archivo`, la aplicación utiliza `tareas.json`.

## 4. Verificación y pruebas

Para comprobar la sintaxis del proyecto:

```bash
python -m compileall -q tareas.py tests
```

Para ejecutar las pruebas automatizadas:

```bash
python -m unittest discover -s tests -v
```

La suite contiene cuatro pruebas: una prueba unitaria y tres pruebas funcionales de la interfaz.

**Resultado de la ejecución local: cuatro pruebas aprobadas.**

## 5. Integración continua

El proyecto utiliza GitHub Actions mediante el archivo:

`.github/workflows/ci.yml`

El flujo automatiza las siguientes actividades:

1. Descarga del repositorio.
2. Configuración de Python 3.12.
3. Compilación del código.
4. Ejecución de las pruebas automatizadas.

El flujo se activa mediante eventos de publicación de cambios (`push`) y solicitudes de integración dirigidas a `main` (`pull_request`).

Las ejecuciones publicadas en GitHub Actions finalizaron satisfactoriamente.

## 6. Control de versiones

Se utilizó Git para gestionar el historial del proyecto y organizar el desarrollo mediante las siguientes ramas:

- `main`: rama principal del proyecto.
- `feature/registro`: desarrollo de la funcionalidad de registro.
- `feature/cli`: desarrollo de la interfaz de consola y pruebas funcionales.

Se publicó la etiqueta de versión `v0.1.0`.

El historial conserva los commits correspondientes al ciclo TDD:

- Rojo: `4a01737`.
- Verde: `667e5b1`.
- Refactorización: `9154238`.

Las funcionalidades desarrolladas en las ramas se integraron en la rama principal mediante merges registrados en el historial de Git.

## 7. Repositorio

Repositorio público:

https://github.com/estefaniaestrada-art/gestor-tareas

En el repositorio se encuentran el código fuente, las pruebas automatizadas, el archivo de configuración de GitHub Actions y el historial de versiones.

## 8. Evidencias

Las evidencias del proyecto incluyen:

- Historial de commits y ramas.
- Ejecución de pruebas unitarias y funcionales.
- Ciclo TDD: rojo, verde y refactorización.
- Ejecuciones exitosas de GitHub Actions.
- Publicación de la etiqueta `v0.1.0`.

