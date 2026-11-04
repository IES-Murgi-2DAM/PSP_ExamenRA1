# Resuelve aquí el ejercicio.
class TareaProceso:

    def __init__(self,nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion

    def supera_limite(self):
        if self.duracion>=5.0:
            return True
        return False


tarea = TareaProceso("backup",6.5)

if tarea.supera_limite():
    print(f"{tarea.nombre}: LARGA")
else:
    print(f"{tarea.nombre}: CORTA")