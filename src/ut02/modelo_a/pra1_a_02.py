from pathlib import Path
import subprocess
import time

script = Path("src/scripts/hijo_pipe.py")

resultado = subprocess.Popen(
    ["python", script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

salida, error =resultado.communicate(input="DATO|copia|archivo-A.zip")
time.sleep(3)
print(f"OUT|{salida}",end="")
print(f"ERR|error")
print(f"RC|resultado.returncode")

resultado2 = subprocess.Popen(
    ["python", script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
#No me da tiempo al timeout
salida, error = resultado2.communicate(input="LENTO")

resultado2.terminate

print("TIMEOUT|CONTROLADO")





# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.
