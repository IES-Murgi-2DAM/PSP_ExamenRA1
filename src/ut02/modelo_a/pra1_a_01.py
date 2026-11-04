from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("exportar-01", "paquete.zip"), ("convertir-02", "ERROR")]

for id, texto in casos:

    resultado = subprocess.run(
        ["python", script, "--tarea", id, "--dato", texto],
        capture_output=True,
        text=True
    )


    if resultado.returncode==0:
        print("OK|", end="")
    else:
        print(f"FALLO|{resultado.returncode}|{texto}|{id}|DATO_INVALIDO",end="")

    print(resultado.stdout)



# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.
