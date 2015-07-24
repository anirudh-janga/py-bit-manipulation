


class BitOperations(object):

    def __init__(self, number):

        #validation
        if number > 255:
            raise TypeError('For now only works for 8 bit numbers')

        self._num = number

    def count_set_bits_1(self):

        #worst case - O(n)
        num_set_bits = 0
        for bit_num in range(8):
            if self._num & (1<<bit_num):
                num_set_bits += 1

        return num_set_bits

    def count_set_bits_2(self):

        number = self._num

        #worst case - O(n)
        num_set_bits = 0
        while number:
            number &= (number-1)
            num_set_bits += 1

        return num_set_bits





