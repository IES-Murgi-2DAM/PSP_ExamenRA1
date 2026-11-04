# Resuelve aquí el ejercicio.

duraciones = [1.2,3.6,2.4,4.1,0.9]

lentas = []

for duracion in duraciones:
    if duracion >= 3.0:
        lentas.append(duracion)
        
print(lentas)