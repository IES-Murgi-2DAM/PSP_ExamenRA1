from functools import reduce
# Resuelve aquí el ejercicio.
def calcular_media(duraciones):
    suma_total = reduce(lambda a , b: a+b, duraciones)
    return f"Media: {suma_total/len(duraciones)}"
print(calcular_media([2.0,3.0,4.0]))