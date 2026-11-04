from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

proceso = subprocess.Popen(["python", script], text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


salida, error = proceso.communicate(input="DATO|copia|archivo-A.zip", timeout=3)

print(f"OUT|{salida.strip()}")
print(f"ERR|{error.strip()}")
print(f"RC|{proceso.returncode}")


proceso2 = subprocess.Popen(["python", script], text=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    salida2, error2 = proceso2.communicate(input="LENTO", timeout=0.2)
except subprocess.TimeoutExpired:
    print("TIMEOUT|CONTROLADO")