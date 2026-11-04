# Resuelve aquí el ejercicio.
class LoteArchivos:
    def ui (selft , nombre , archivos):
        selft.nombre = nombre
        selft.archivos = archivos
    def resumen(selft):
        cantidad = len(selft.archivos)
        return f"{selft.nombre}: {cantidad} archivos"
lote = LoteArchivos("backup",["informe.txt","copia.zip","datos.csv"])
print(lote.resumen)