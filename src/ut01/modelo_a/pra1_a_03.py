# Resuelve aquí el ejercicio.
class TareaProceso:

    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def supera_limite(self):
        if self.duracion >= 5.0:
            return True
        else:
            return False


tarea_proceso = TareaProceso("backup", 6.5)

if tarea_proceso.supera_limite():
    print(f"{tarea_proceso.nombre}: LARGA")
else:
    print(f"{tarea_proceso.nombre}: NORMAL")
