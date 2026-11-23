def tarea_nueva(titulo):
    return {"titulo": titulo.strip(), "hecha": False}

def registrar(tareas, titulo):
    return tareas + [tarea_nueva(titulo)]

import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archivo", type=Path, default=Path("tareas.json"))
    comandos = parser.add_subparsers(dest="accion", required=True)
    alta = comandos.add_parser("agregar")
    alta.add_argument("titulo")
    comandos.add_parser("listar")
    args = parser.parse_args()
    if args.accion == "agregar" and not args.titulo.strip():
        parser.error("El título es obligatorio")
    tareas = json.loads(args.archivo.read_text(encoding="utf-8")) if args.archivo.exists() else []
    if args.accion == "agregar":
        tareas = registrar(tareas, args.titulo)
        args.archivo.write_text(json.dumps(tareas, ensure_ascii=False), encoding="utf-8")
    else:
        for tarea in tareas:
            print(f"[pendiente] {tarea['titulo']}")

if __name__ == "__main__":
    main()
