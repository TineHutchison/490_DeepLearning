"""
Adds "noise" to a given array by randomly flipping bits on the array.
Returns a new Letter object.
"""
from random import random
from .Letter import Letter

def add_noise(lettr, noise_level):
    new_array = []

    def _flip_bit(bit):
        if bit == 0:
            return 1
        else:
            return 0

    for pixel in lettr.array:
        if random() <= noise_level:
            new_array.append(_flip_bit(pixel))
        else:
            new_array.append(pixel)

    return Letter(new_array, lettr.letter)
