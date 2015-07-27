import unittest
from code import next_power_of_2

class TestCases(unittest.TestCase):

    def setUp(self):
        self.obj = next_power_of_2.NextPow2(6)

    def test_case_1(self):
        self.assertEqual(self.obj.next_pow_2(), 8)
