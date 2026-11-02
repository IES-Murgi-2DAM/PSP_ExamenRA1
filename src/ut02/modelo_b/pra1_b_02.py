from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

def ejecutar_proceso(proceso, entrada, timeout):
    try:
        salida, error = proceso.communicate(input=entrada, timeout=timeout)
        print(f"OUT|{salida.strip()}")
        print(f"ERR|{error.strip()}")
        print(f"RC|{proceso.poll()}")
    except subprocess.TimeoutExpired:
        proceso.terminate()
        proceso.communicate()
        print("TIMEOUT|CONTROLADO")

proceso = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
ejecutar_proceso(proceso, "DATO|conversion|archivo-B.zip", 3)

proceso = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
ejecutar_proceso(proceso, "LENTO", 0.2)
