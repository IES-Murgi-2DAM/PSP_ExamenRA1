# Resuelve aquí el ejercicio.
def nombres_en_mayusculas(nombres):
    nombresMayuscula = []
    for nombre in nombres:
        nombresMayuscula.append(nombre.upper())
    return nombresMayuscula

nombres = nombres_en_mayusculas(["informe.txt", "copia.zip", "datos.csv"])
print (nombres)