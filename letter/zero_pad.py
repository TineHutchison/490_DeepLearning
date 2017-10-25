from .Letter import Letter

def zero_pad(lettr):
    """ Build zero padding around provided Letter object

    :param lettr: a Letter object
    :return: a new Letter object
    """
    new_root = lettr.root + 2
    new_array = [0 for i in range(new_root)]
    for idx, pixel in enumerate(lettr.array):
        if idx == 0 | idx == len(lettr.array) + 1:
            new_array.append(0)
        elif idx % lettr.root == 0:
            new_array.extend([0,0])
        new_array.append(pixel)
    new_array.extend([0 for i in range(new_root + 1)])

