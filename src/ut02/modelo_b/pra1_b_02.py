from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

resultado = subprocess.Popen(["python","-c"], stdin = subprocess.PIPE, stdout=subprocess.PIPE,text= True)

if resultado.returncode == 0:
    print("OK")
else:
    print("FALLO")