# Resuelve aquí el ejercicio.
class TareaProceso:
    nombre = ""
    duracion = 0.0

    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def supera_limite(self):
        return self.duracion >= 5.0

tarea = TareaProceso("backup", 6.5)
if tarea.supera_limite():
    print(f"{tarea.nombre}: LARGA")
else:
    print(f"{tarea.nombre}: NORMAL")

