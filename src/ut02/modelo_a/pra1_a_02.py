from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

proceso = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
salida, error = proceso.communicate(input="DATO|copia|archivo-A.zip", timeout=3)
print(f"OUT|{salida.strip()}")
print(f"ERR|{error.strip()}")
print(f"RC|{proceso.returncode}")

proceso = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
try:
    salida, error = proceso.communicate(input="LENTO", timeout=0.2)
except subprocess.TimeoutExpired:
    proceso.terminate()
    proceso.communicate()
    print("TIMEOUT|CONTROLADO")
