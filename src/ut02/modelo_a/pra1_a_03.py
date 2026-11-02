from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("A-01", 12, False), ("A-02", 7, True), ("A-03", 5, False)]
procesos = []

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.
