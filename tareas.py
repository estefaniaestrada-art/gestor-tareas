def tarea_nueva(titulo):
    return {"titulo": titulo.strip(), "hecha": False}

def registrar(tareas, titulo):
    return tareas + [tarea_nueva(titulo)]
