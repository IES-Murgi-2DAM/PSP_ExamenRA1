from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("exportar-01", "paquete.zip"), ("convertir-02", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,resultado

resultado = subprocess.run(["python"]), capture_output=True, text=True
casos = {0: "OK", 1:"FALLO"}
for id, texto in casos:


#print(f"OK, {resultado})

# capturar sus dos canales de salida y examinar returncode.
