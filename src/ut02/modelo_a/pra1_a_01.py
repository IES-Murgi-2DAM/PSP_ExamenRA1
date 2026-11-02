from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("exportar-01", "paquete.zip"), ("convertir-02", "ERROR")]

for id, texto in casos:
    proceso = subprocess.run(["python", script, "--tarea", id, "--dato", texto], capture_output=True, text=True)
    if proceso.returncode == 0:
        print(f"OK|{proceso.stdout.strip()}")
    else:
        print(f"FALLO|{proceso.returncode}|{proceso.stderr.strip()}")
