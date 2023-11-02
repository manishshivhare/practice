import re
import unittest


def rearrange_name(name):
    result = re.search(r"^([\w+ .]*), ([\w+ .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Shivhare, Manish"
        expected = "Manish Shivhare"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_one_name(self):
        testcase = "Harry"
        expected = "Harry" 
        self.assertEqual(rearrange_name(testcase), expected) 
    def test_invalid_name(self):
        self.assertRaises(ValueError, rearrange_name, 145)

unittest.main()
