"""Strict parsing of Roman numerals: what is this numeral actually worth?

Most "Roman numeral parsers" people write online are lenient about things a
Roman scribe never would have written (IIII, VX, IC). This one is not. If
value_of() accepts a string, the string is the one correct way to write that
number in the range it supports.
"""

import re

_NUMERAL_PATTERN = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)

_VALUES = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000,
}

_SUBTRACTIVE_PAIRS = ("CM", "CD", "XC", "XL", "IX", "IV")


class RomanNumeralError(ValueError):
    """Raised when a string is not a well-formed Roman numeral."""


def value_of(text: str) -> int:
    """Return the integer value of a strictly well-formed Roman numeral.

    Valid range is I to MMMCMXCIX (1 to 3999); larger numbers need an
    overline notation this tool doesn't support. Rejects repeated
    subtractive pairs, out-of-order subtraction, lowercase, whitespace,
    and the empty string (there is no Roman numeral for zero).
    """
    if not _NUMERAL_PATTERN.match(text):
        raise RomanNumeralError(f"{text!r} is not a well-formed Roman numeral")

    total = 0
    i = 0
    while i < len(text):
        pair = text[i:i + 2]
        if pair in _SUBTRACTIVE_PAIRS:
            total += _VALUES[pair[1]] - _VALUES[pair[0]]
            i += 2
        else:
            total += _VALUES[text[i]]
            i += 1
    return total
