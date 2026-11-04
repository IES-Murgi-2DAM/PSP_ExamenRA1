from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

proc = subprocess.Popen(["python" , str(script)],stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr= subprocess.PIPE ,text = True)

try: 
    out , err = proc.communicate ("DATO| conversion| archivo-B.zip", timeout = 3)
    print(f"OUT| {out.strip()}")
    print(f"ERR| {err.strip()}")
    print(f"RC| {proc.returncode}")

except subprocess.TimeoutExpired:
    proc.terminate() 
    proc.communicate
    print("TIMEOUT| NO_ESPERADO")

proc2 = subprocess.Popen (["python",script], stdin = subprocess.PIPE , stdout = subprocess.PIPE , stderr= subprocess.PIPE, text = True)

try: 
    out2, err2 = proc2.communicate ("LENTO" , timeout= 0.2)
    print(f"OUT| {out2.strip()}")
except subprocess.TimeoutExpired:
    proc2.terminate()
    proc2.communicate
    print("TIMEOUT|CONTROLADO")