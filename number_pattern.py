"""Build a space-separated number pattern string.

number_pattern(n) validates its input and returns the numbers 1..n
joined with spaces, e.g. number_pattern(5) -> "1 2 3 4 5".

Validation rules (checked in order):
  1. n must be an int (bools, floats, strings, ... are rejected)
  2. n must be greater than 0
"""


def number_pattern(n: int) -> str:
    """Return the numbers 1..n joined with spaces, or an error message."""
    if type(n) is not int:
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    return " ".join(result)


if __name__ == "__main__":
    for demo in (5, 1, 0, -3, 3.5, "5", True, None):
        print(f"number_pattern({demo!r}) -> {number_pattern(demo)!r}")
