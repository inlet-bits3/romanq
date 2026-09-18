import unittest

from romanq.core import RomanNumeralError, value_of

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


if __name__ == "__main__":
    unittest.main()
