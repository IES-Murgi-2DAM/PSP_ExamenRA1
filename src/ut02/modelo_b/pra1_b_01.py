from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("backup-04", "copia.tar"), ("convertir-05", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.

for tarea_id, dato in casos:
    proc = subprocess.run(["python" , script ,"--tarea", tarea_id, "--dato",dato],capture_output=True , text=True)
    if proc.returncode == 0:
        print(f"OK| {proc.stdout.strip()}")
    else:
        print(f"FALLO| {proc.returncode} | {proc.stderr.strip()}")