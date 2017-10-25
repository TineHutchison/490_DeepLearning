from .Letter import Letter

def load_letters(size=25, one_example_per_letter=False):
    """ Load all letters of given size (25, 81, etc)

    :param size:
    :param one_example_per_letter:
    :return: number of unique letters and a list of Letter objects
    """
    from os import listdir
    from os.path import dirname, realpath
    basedir = dirname(realpath(__file__))

    if size == 25:
        alpha_dir = basedir + '/5x5_alphabet/'
    elif size == 81:
        alpha_dir = basedir + '/9x9_alphabet/'

    letters = [f for f in listdir(alpha_dir) if f[0] != '.']
    letter_objects = []

    for letter in letters:
        letter_dir = alpha_dir + letter + '/'
        count = 0
        for instance in [f for f in listdir(letter_dir)]:
            instance_array = []
            if one_example_per_letter & (count > 0):
                continue
            with open(letter_dir + instance) as f:
                for line in f:
                    if '#' not in line:
                        instance_array.extend(line.replace(' ','').replace(',','').replace('\n',''))
            letter_objects.append(Letter([int(x) for x in instance_array],letter))
            count += 1

    return len(letters), letter_objects
