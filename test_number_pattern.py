import unittest

from number_pattern import number_pattern


class TestNumberPattern(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(number_pattern(5), "1 2 3 4 5")

    def test_single(self):
        self.assertEqual(number_pattern(1), "1")

    def test_zero_rejected(self):
        self.assertEqual(number_pattern(0), "Argument must be an integer greater than 0.")

    def test_negative_rejected(self):
        self.assertEqual(number_pattern(-3), "Argument must be an integer greater than 0.")

    def test_float_rejected(self):
        self.assertEqual(number_pattern(3.5), "Argument must be an integer value.")

    def test_string_rejected(self):
        self.assertEqual(number_pattern("5"), "Argument must be an integer value.")

    def test_bool_rejected(self):
        # type(n) is not int (not isinstance) so True is rejected too
        self.assertEqual(number_pattern(True), "Argument must be an integer value.")

    def test_none_rejected(self):
        self.assertEqual(number_pattern(None), "Argument must be an integer value.")


if __name__ == "__main__":
    unittest.main()
