class TareaProceso:

    def __init__(self, nombre, duracion):
        self.nombre=nombre
        self.duracion=duracion
    @classmethod
    def supera_limite(duracion):
        if duracion >= 5.0:
            return True
        else:
            return False
        
p = TareaProceso("backup",6.5)

