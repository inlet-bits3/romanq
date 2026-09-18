import sys

from .core import RomanNumeralError, value_of


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage: romanq NUMERAL", file=sys.stderr)
        return 2

    try:
        print(value_of(argv[0]))
    except RomanNumeralError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
