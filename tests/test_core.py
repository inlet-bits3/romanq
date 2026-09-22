import unittest

from romanq.core import RomanNumeralError, to_roman, value_of

VALID_CASES = [
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("V", 5),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),
    ("MCMXCIV", 1994),      # the classic textbook hard case
    ("MMXXIV", 2024),
    ("MMMCMXCIX", 3999),    # top of the strict range
    ("LVIII", 58),
    ("DCLXVI", 666),
]

INVALID_CASES = [
    "",          # nothing is not a numeral
    "IIII",      # four ones should be IV, not repeated I
    "VV",        # V never repeats
    "IC",        # 99 is XCIX, not a jump straight to C
    "IM",        # same problem, jumping to M
    "VX",        # V can't subtract from X
    "IXI",       # nothing follows a subtractive pair
    "MMMM",      # four thousands, past the strict range
    "iv",        # lowercase
    "IV ",       # trailing whitespace
    " IV",       # leading whitespace
    "MCMC",      # two subtractive C-groups in the hundreds place
    "XIVX",      # garbage after a valid prefix
    "ABC",       # not Roman numeral letters at all
    "0",         # there is no Roman numeral for zero
]


INVALID_INTEGERS = [
    0,            # no Roman numeral for zero
    -1,           # no negative numerals
    4000,         # past the strict range
    1.5,          # not an integer at all
    True,         # bool is technically an int subclass, but not a number here
]


class ValueOfTests(unittest.TestCase):
    def test_valid_numerals(self):
        for numeral, expected in VALID_CASES:
            with self.subTest(numeral=numeral):
                self.assertEqual(value_of(numeral), expected)

    def test_invalid_numerals(self):
        for numeral in INVALID_CASES:
            with self.subTest(numeral=numeral):
                with self.assertRaises(RomanNumeralError):
                    value_of(numeral)


class ToRomanTests(unittest.TestCase):
    def test_valid_integers(self):
        for numeral, value in VALID_CASES:
            with self.subTest(value=value):
                self.assertEqual(to_roman(value), numeral)

    def test_invalid_integers(self):
        for number in INVALID_INTEGERS:
            with self.subTest(number=number):
                with self.assertRaises(RomanNumeralError):
                    to_roman(number)

    def test_round_trip(self):
        for number in range(1, 4000):
            with self.subTest(number=number):
                self.assertEqual(value_of(to_roman(number)), number)


if __name__ == "__main__":
    unittest.main()
