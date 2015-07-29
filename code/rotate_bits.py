

class BitOperations(object):

    def __init__(self, number):
        self._num = number

    def rotate_right(self, num_times):
        n = self._num
        return (n >> num_times) | (n <<(64 - num_times))

    def rotate_left(self, num_times):
        n = self._num
        return (n << num_times) | (n >> (64 - num_times))

