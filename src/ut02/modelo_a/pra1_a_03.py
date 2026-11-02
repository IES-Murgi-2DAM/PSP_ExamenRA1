from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("A-01", 12, False), ("A-02", 7, True), ("A-03", 5, False)]
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
        code = proceso.returncode
        if code == 0:
            print(f"{id}|OK|{salida.strip()}")
        else:
            print(f"{id}|ERROR|{code}|{error.strip()}")
    except subprocess.TimeoutExpired:
        proceso.terminate()
        proceso.communicate()
        print("TIMEOUT|CONTROLADO")
