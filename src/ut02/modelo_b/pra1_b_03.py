from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("B-11", 9, False), ("B-12", 4, False), ("B-13", 6, True)]
procesos = []

for id, valor, fallo in tareas:
    if not fallo:
        procesos.append((id, subprocess.Popen(["python", script, "--id", id, "--valor", str(valor), "--retardo-ms", "200"],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)))
    else:
        procesos.append((id, subprocess.Popen(["python", script, "--id", id, "--valor", str(valor), "--fallo", "--retardo-ms", "200"],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)))

for id, proceso in procesos:
    try:
        salida, error = proceso.communicate(timeout=3)
        code = proceso.poll()
        if code == 0:
            print(f"{id}|OK|{salida.strip()}")
        else:
            print(f"{id}|ERROR|{code}|{error.strip()}")
    except subprocess.TimeoutExpired:
        proceso.terminate()
        proceso.communicate()
        print("TIMEOUT|CONTROLADO")