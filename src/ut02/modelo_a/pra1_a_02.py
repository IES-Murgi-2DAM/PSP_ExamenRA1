from asyncio import timeout
from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.
proceso=subprocess.Popen(["DATO"])
proceso=subprocess.Popen(["RECIBIDO"])

stdin=subprocess.PIPE,
stdout=subprocess.PIPE, text=True
salida, _comunicate=proceso.communicate(input="DATO|copia|archivo-A.zip")
salida, _comunicate=proceso.communicate(input="REGISTRO")
timeout(3)