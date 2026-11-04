from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("B-11", 9, False), ("B-12", 4, False), ("B-13", 6, True)]
procesos = []

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.

for tarea_id , valor , fallo in tareas : 
    c = ["python" , script, "--id" , tarea_id, "--valor" , str(valor),"retardo-ms", "200"]
    if fallo:
        c.append("--fallo")
    proc = subprocess.Popen (c , stdount = subprocess.PIPE , stderr=subprocess.PIPE , text = True)
    procesos.append((tarea_id , proc))

for tarea_id proc in procesos: 
    try:
        out , err = proc.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        proc.terminate()
        out , err = proc.communicate()
        print(f"{tarea_id}|ERROR|TIMEOUT")