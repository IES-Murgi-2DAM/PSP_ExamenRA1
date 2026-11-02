import sys
import time


def main():
    linea = sys.stdin.readline().rstrip("\r\n")

    if linea.startswith("DATO|"):
        print(f"RECIBIDO|{linea[len('DATO|'):]}")
        print("REGISTRO|OK", file=sys.stderr)
        return 0

    if linea == "LENTO":
        time.sleep(2)
        print("RECIBIDO|LENTO")
        return 0

    print("ERROR|ENTRADA_INVALIDA", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
