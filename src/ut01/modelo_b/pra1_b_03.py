# Resuelve aquí el ejercicio.
class LoteArchivos():
    def __init__(self, nombre, archivos = []):
        self.nombre = nombre
        self.archivos = archivos

    def resumen(self):
        return (str(f"{self.nombre}: {len(self.archivos)} archivos"))

print(LoteArchivos("backup", ["informe.txt", "copia.zip", "datos.csv"]).resumen())