from math import sqrt
class Letter(object):
    def __init__(self, flattened_letter_array, target_letter):
        self.array = flattened_letter_array
        self.root = sqrt(len(flattened_letter_array))
        self.letter = target_letter
        self.target = ord(self.letter.lower()) - 97
        self.bigclass = self._big_class()

    def _big_class(self):
        if self.letter in 'AKMNVWXY':
            return 'AKMNVWXY'
        if self.letter in 'BEFHLPRSZ':
            return 'BEFHLPRSZ'
        if self.letter in 'CDGOQU':
            return 'CDGOQU'
        if self.letter in 'IJT':
            return 'IJT'

    def print_array(self):
        for idx, pixel in enumerate(self.array):
            if idx % self.root == 0:
                print('\n'),
            print(pixel),



