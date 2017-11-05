"""
Takes a Letter object and 'down samples' to reduce the size of the matrix.
Looks for a local maximum in a 3x3 subsample of the input letter.
Tends to create arrays that are 2 pixels smaller in both dimensions, so a
9x9 array becomes a 7x7 array.
"""
from .Letter import Letter
from numpy import array
from numpy import reshape

def down_sample(input_lettr):
    old_array = reshape(input_lettr.array,(int(input_lettr.root),int(input_lettr.root)))
    new_list = []
    height, width = old_array.shape
    for h in range(height - 2):
        for w in range(width - 2):
            new_list.append(old_array[h:h+3, w:w+3].max())
    return Letter(new_list, input_lettr.letter)
