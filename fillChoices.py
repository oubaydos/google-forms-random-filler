import random

L = dict()


def fill_choices(entry_id, possible_values):
    L[entry_id] = possible_values


def get_random_choice(entry_id):
    if entry_id not in L.keys():
        print("key does not exist")
        return
    return random.choice(L.get(entry_id))


def get_random_choices():
    rst = []
    for i in L.keys():
        rst.append(random.choice(L.get(i)))
    return rst
