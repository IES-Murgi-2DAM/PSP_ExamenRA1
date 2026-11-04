from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("B-11", 9, False), ("B-12", 4, False), ("B-13", 6, True)]
procesos = []

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.

for tarea in tareas:
    id, valor, fallo = tarea
    if fallo==True:
        procesos.append(subprocess.Popen(["python", script, "--id", id, "--valor", str(valor), "--fallo", "--retardo-ms", "200"], stdin=subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True))
    else: 
        procesos.append(subprocess.Popen(["python", script, "--id", id, "--valor", str(valor), "--retardo-ms", "200"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
for proceso in procesos:
    string, error =proceso.communicate(input="")
    string.strip()
    error.strip()
    print(string)
    if error!= "":
        print(error)
    