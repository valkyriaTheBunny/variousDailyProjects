import random

def pickRandom(stream):
    random_element = None
    for i, e in enumerate(stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element