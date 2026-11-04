from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("backup-04", "copia.tar"), ("convertir-05", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.


for caso in casos:
    tarea, dato= caso
    proceso = subprocess.run(["python", script, "--tarea", tarea, "--dato", dato], capture_output=True, text=True)
    if proceso.returncode == 0:
        print(f"OK|{proceso.stdout}")
    else:
        print(f"FALLO|{proceso.returncode}|{proceso.stderr}")
