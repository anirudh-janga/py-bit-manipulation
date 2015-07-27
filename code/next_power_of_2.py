
class NextPow2(object):

    def __init__(self, number):
        self._num = number

    def next_pow_2(self):
        n = self._num
        n |= n>>1
        n |= n>>2
        n |= n>>4
        n |= n>>8
        n |= n>>16
        return n+1


