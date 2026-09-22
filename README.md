# romanq

A command-line tool that answers exactly one question: what integer does
this Roman numeral mean, and is it even a real one? It also goes the other
way: given an integer, what's the one correct numeral for it?

Most "Roman numeral converter" snippets you find online will happily accept
`IIII` for 4 or `IC` for 99. Those aren't Roman numerals, they're strings
that happen to be made of the same letters. `romanq` only accepts a numeral
if it's the single correct way to write that number, in the range I to
MMMCMXCIX (1 to 3999 — beyond that the Romans used an overline notation this
tool doesn't support).

## Usage

```
$ romanq MCMXCIV
1994

$ romanq IIII
error: 'IIII' is not a well-formed Roman numeral

$ romanq mmxxiv
error: 'mmxxiv' is not a well-formed Roman numeral

$ romanq 1994
MCMXCIV

$ romanq 4000
error: 4000 is out of range (1-3999, no Roman numeral for 0 or anything above MMMCMXCIX)
```

`romanq` picks the direction based on the shape of its argument: something
that parses as an integer goes through `to_roman`, anything else is treated
as a numeral and goes through `value_of`.

As a library:

```python
from romanq import value_of, to_roman, RomanNumeralError

value_of("MMXXIV")  # 2024
to_roman(2024)       # "MMXXIV"

try:
    value_of("IC")
except RomanNumeralError as exc:
    print(exc)
```

## Install

No dependencies. Clone it and either run the module directly:

```
python -m romanq.cli MCMXCIV
```

or install it locally so the `romanq` command is on your path:

```
pip install -e .
```

## Running the tests

```
python -m unittest discover tests
```

The test suite is table-driven on purpose — the interesting bugs in Roman
numeral parsing all live in the awkward cases (repeated subtractive pairs,
out-of-order subtraction, whitespace, lowercase), so the tables are where
the actual coverage lives.
