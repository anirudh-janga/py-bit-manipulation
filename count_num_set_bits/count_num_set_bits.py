


class BitOperations(object):

    def __init__(self, number):

        #validation
        if number > 255:
            raise TypeError('For now only works for 8 bit numbers')

        self._num = number

        #build a look up table
        bit_table = [0]*256
        for index in range(256):
            bit_table[index] = (index&1) + bit_table[index>>1]
        self.bit_table = bit_table

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

    def count_set_bits_3(self):

        #worst case - O(1)
        return self.bit_table[self._num & 0xff]




