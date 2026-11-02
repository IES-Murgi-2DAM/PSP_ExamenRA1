# Resuelve aquí el ejercicio.
def nombres_en_mayusculas(nombres):
    mayus = []
    for nombre in nombres:
        mayus.append(nombre.upper())

    return mayus

print(nombres_en_mayusculas(['informe.txt', 'copia.zip', 'datos.csv']))
