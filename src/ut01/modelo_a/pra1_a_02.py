# Resuelve aquí el ejercicio.
def calcular_media(duraciones):
    suma = 0.0
    for duracion in duraciones:
        suma = suma + duracion

    return suma / len(duraciones)

media = calcular_media([2.0, 3.0, 4.0])
print(f"Media: {media}")