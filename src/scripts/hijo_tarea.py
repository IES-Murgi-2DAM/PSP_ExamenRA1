import argparse
import sys
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--valor", required=True, type=int)
    parser.add_argument("--fallo", action="store_true")
    parser.add_argument("--retardo-ms", type=int, default=0)
    args = parser.parse_args()

    if args.retardo_ms < 0:
        parser.error("--retardo-ms no puede ser negativo")

    time.sleep(args.retardo_ms / 1000)

    if args.fallo:
        print(f"ERROR|{args.id}|FALLO_SIMULADO", file=sys.stderr)
        return 5

    print(f"RESULTADO|{args.id}|{args.valor * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
