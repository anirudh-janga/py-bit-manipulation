import unittest
from code import rotate_bits

class TestRotateBits(unittest.TestCase):

    def setUp(self):
        self.obj = rotate_bits.BitOperations(0b10000000)

    def test_rotate_left(self):
        answer = self.obj.rotate_left(2)
        expected_result = 0b00000010
        self.assertEqual(answer, expected_result)

    def test_rotate_right(self):
        answer = self.obj.rotate_right(2)
        expected_result = 0b00100000
        self.assertEqual(answer, expected_result)
