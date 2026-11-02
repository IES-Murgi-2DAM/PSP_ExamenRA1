from pathlib import Path
import subprocess
import sys

script = Path("src/scripts/hijo_resultado.py")
casos = [("backup-04", "copia.tar"), ("convertir-05", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.
