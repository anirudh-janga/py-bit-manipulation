'''
Set of all bit wise operations
'''

class BitOperations(object):
    '''
    Initiaze the bit operations object
    '''

    def __init__(self, number):
        self._number = number

    def is_bit_on(self, bit_num):
        return self._number & (1 << bit_num)

    def set_bit(self, bit_num):
        return self._number | (1 << bit_num)

    def clear_bit(self, bit_num):
        return self._number & ~(1 << bit_num)

    def flip_bit(self, bit_num):
        return self._number ^ (1 << bit_num)

    def clear_last_set_bit(self):
        return self._number & (self._number-1)




