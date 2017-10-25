from .Letter import Letter
from random import choice
def get_one_example_per_letter(all_letters):
    letters = set([l.letter for l in all_letters])
    letter_objects = []
    while len(letters) > 0:
        let = choice(all_letters)
        if let.letter in letters:
            letter_objects.append(let)
            letters.remove(let.letter)
    return letter_objects
