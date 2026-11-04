# Resuelve aquí el ejercicio.
def calcular_media(duraciones):

    total = 0
    
    for duracion in duraciones:
        total += duracion

    return total / len(duraciones)


lista_duraciones = [2.0, 3.0, 4.0]

print(f"Media: {calcular_media(lista_duraciones)}")