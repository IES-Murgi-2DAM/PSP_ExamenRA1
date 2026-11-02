from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("exportar-01", "paquete.zip"), ("convertir-02", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.
