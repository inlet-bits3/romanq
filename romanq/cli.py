import sys

from .core import RomanNumeralError, to_roman, value_of


def _looks_like_integer(text: str) -> bool:
    body = text[1:] if text.startswith("-") else text
    return body.isdigit()


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage: romanq NUMERAL | romanq INTEGER", file=sys.stderr)
        return 2

    arg = argv[0]
    try:
        if _looks_like_integer(arg):
            print(to_roman(int(arg)))
        else:
            print(value_of(arg))
    except RomanNumeralError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
