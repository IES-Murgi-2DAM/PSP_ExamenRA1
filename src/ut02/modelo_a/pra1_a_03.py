from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("A-01", 12, False), ("A-02", 7, True), ("A-03", 5, False)]
procesos = []

for id ,valor,resultado in tareas:

    try:
        resultado = subprocess.Popen(
            ["python", script, "--id", id, "--valor", valor],
            capture_output=True,
            text=True
        )


    except subprocess.TimeoutExpired:
        print("Termino el proceso")

print()

#Estoy mirando el 8 pero entre los comandos y lo otro no da tiempo  ;(

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.
