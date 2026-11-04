# Resuelve aquí el ejercicio.
def nombres_en_mayusculas(nombres):
    mayusculas=[]
    for nombre in nombres:
        mayusculas.append(nombre.upper())
    return mayusculas
resu = nombres_en_mayusculas (["informe.txt", "copia.zip","datos.csv"])
print(resu)