# Gestor de tareas por consola

Proyecto de integración continua de Estefanía Estrada Pérez, Corporación Universitaria del Caribe (CECAR). Registra tareas pendientes y las guarda en un archivo JSON para consultarlas en otra sesión.

## Requisitos y ejecución

Se necesita Python 3.12 y Git para trabajar con el historial. La aplicación y las pruebas usan la biblioteca estándar.

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python tareas.py --archivo ejemplo.json agregar "  Estudiar  "
python tareas.py --archivo ejemplo.json listar
```

La segunda orden imprime `[pendiente] Estudiar`. Omite `--archivo ejemplo.json` para usar `tareas.json`. El ejemplo crea datos locales. En Windows se puede invocar `.venv\Scripts\python.exe` directamente.

## Verificación

```bash
python -m compileall -q tareas.py tests
python -m unittest discover -s tests -v
```

La suite incluye una prueba unitaria y tres pruebas funcionales de la interfaz. El flujo de GitHub Actions en `.github/workflows/ci.yml` repite estas verificaciones al publicar cambios y en las solicitudes dirigidas a `main`.

## Historial y evidencias

El archivo `gestor-tareas.bundle` conserva las ramas y los commits locales. Desde la carpeta donde se extrajo el ZIP:

```bash
git clone gestor-tareas.bundle gestor-tareas
cd gestor-tareas
git log --graph --all --oneline --decorate
```

Los commits `4a01737`, `667e5b1` y `9154238` corresponden a las fases roja, verde y de refactorización. Para repetirlas sin mover la rama principal, usa un worktree temporal para cada commit y ejecuta allí el descubrimiento de pruebas. La carpeta externa `evidencias/` contiene las salidas originales de la demostración local.

## GitHub y entrega

Crea el repositorio del grupo en GitHub con la visibilidad que corresponda. Si Git creó un remoto `origin` al clonar el bundle, actualízalo y publica la rama principal. Las ramas originales de la demostración ya están integradas localmente. Para evidenciar una solicitud efectiva en GitHub, crea una rama nueva con una mejora real, abre una solicitud hacia `main` y espera la ejecución automática antes de integrar.

```bash
git remote set-url origin URL_REAL_DE_GITHUB
git push -u origin main
git push origin v0.1.0
```

En un repositorio privado, agrega a la docente como colaboradora. Incluye la URL real, la solicitud integrada y la ejecución de Actions en el anexo A del informe.
