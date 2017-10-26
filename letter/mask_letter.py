"""
Takes a one dimensional array, temporarily converts to 2d.
Applies a mask to show:
    Vertical lines: |
    Horizontal lines: -
    Upper Left diag: \\  (has to be escaped to work...)
    Upper Right diag: /
Returns a new Letter object.
"""
from .Letter import Letter
from .zero_pad import zero_pad
from numpy import array
from numpy import reshape

def mask_letter(lettr, mask):
    lettr = zero_pad(lettr)
    mask_ = create_mask(mask)
    old_array = reshape(lettr.array,(int(lettr.root),int(lettr.root)))
    new_list = []
    height, width = old_array.shape
    for h in range(height - 2):
        for w in range(width - 2):
            new_list.append(sum(sum(mask_ * old_array[h:h+3, w:w+3])) / 3.0)
    return Letter(new_list, lettr.letter)



def create_mask(mask):
    if mask == '-':
        return array([[0,0,0],[1,1,1],[0,0,0]])
    elif mask == '|':
        return array([[0,1,0],[0,1,0],[0,1,0]])
    elif mask == "\\":
        return array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    else:  # mask == '/'
        return array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
