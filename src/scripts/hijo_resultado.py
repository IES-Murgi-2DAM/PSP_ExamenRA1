import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tarea", required=True)
    parser.add_argument("--dato", required=True)
    args = parser.parse_args()

    if args.dato == "ERROR":
        print(f"ERROR|{args.tarea}|DATO_INVALIDO", file=sys.stderr)
        return 2

    print(f"RESULTADO|{args.tarea}|{args.dato}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
