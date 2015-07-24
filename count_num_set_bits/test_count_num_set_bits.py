import unittest

import count_num_set_bits

class TestCountNumBits(unittest.TestCase):

    def setUp(self):
        self.obj = count_num_set_bits.BitOperations(0b11101100)

    def test_count_set_bits_implementation_1(self):
        self.assertEqual(self.obj.count_set_bits_1(), 5)

    def test_count_set_bits_implementation_2(self):
        self.assertEqual(self.obj.count_set_bits_2(), 5)


if __name__ == "__main__":
    unittest.main()
