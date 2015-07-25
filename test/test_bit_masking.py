import unittest

from code import bit_masking

class TestBitManipulation(unittest.TestCase):

    def setUp(self):
        self.obj = bit_masking.BitOperations(0b11001100)

    def test_is_bit_on(self):
        self.assertTrue(self.obj.is_bit_on(3))

    def test_set_bit(self):
        num = self.obj.set_bit(0)
        self.assertEqual(num, 0b11001101)

    def test_clear_bit(self):
        num = self.obj.clear_bit(2)
        self.assertEqual(num, 0b11001000)

    def test_flip_bit_case1(self):
        num_1 = self.obj.flip_bit(0)
        self.assertEqual(num_1, 0b11001101)

    def test_flip_bit_case2(self):
        num_2 = self.obj.flip_bit(7)
        self.assertEqual(num_2, 0b01001100)

    def test_clear_last_set_bit(self):
        num = self.obj.clear_last_set_bit()
        self.assertEqual(num, 0b11001000)

if __name__ == "__main__":
    unittest.main()


