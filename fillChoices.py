import random

from usefullData import *
from logger import logging

L = dict()
probabilities = dict()
global_name_id = ""
phone_number_id = ""


def fill_choices(entry_id: str, possible_values: list, name_entry_id="", phone_number_entry_id=""):
    """fill list of possible choices (uniformly distributed)"""
    L[entry_id] = possible_values
    global global_name_id, phone_number_id
    if global_name_id == "":
        global_name_id = name_entry_id
    if phone_number_id == "":
        phone_number_id = phone_number_entry_id


def get_random_choice(entry_id: str):
    """get a random uniform choice for entry_id"""
    if check_if_entry_is_name_or_id(entry_id):
        return check_if_entry_is_name_or_id(entry_id)
    if not validate_entry_id(entry_id):
        return
    return random.choice(L.get(entry_id))


def get_random_choices():
    """get randomly uniform choices """
    rst = dict()
    for i in L.keys():
        if not check_if_entry_is_name_or_id(i):
            rst[i] = random.choice(L.get(i))
    if global_name_id != "":
        rst[global_name_id] = check_if_entry_is_name_or_id(global_name_id)
    if phone_number_id != "":
        rst[phone_number_id] = check_if_entry_is_name_or_id(phone_number_id)
    return rst


def update_probability(entry_id: str, probability: list):
    """update or add the list of probabilities for a certain entry_id"""
    if not validate_entry_id(entry_id):
        return
    probabilities[entry_id] = probability


def fill_choices_with_probability(entry_id: str, possible_values: list, each_probability: list, name_entry_id="",
                                  phone_number_entry_id=""):
    """fill the choices with probabilities to use with weighted random choices generator
    """
    fill_choices(entry_id, possible_values, name_entry_id, phone_number_entry_id)
    probabilities[entry_id] = each_probability


def get_random_choice_with_probability(entry_id: str, number_of_items=1):
    """get :args:number_of_items of weighted random data to fill in the form with"""
    if not validate_entry_id(entry_id):
        return
    if entry_id not in probabilities:
        logging.error("key does not have a probability")
        return
    temp_list = random.choices(population=L.get(entry_id), weights=probabilities.get(entry_id), k=number_of_items)
    # if name_id != "":
    #     for i in temp_list:
    #         i. ?? dict

    return temp_list


def validate_entry_id(entry_id: str):
    """check if entry exists"""
    if entry_id in L.keys():
        return True
    print("key does not exist")
    return False


def specify_name_entry(entry_id: str):
    """specifies the entry that should contains random names"""
    global global_name_id
    global_name_id = entry_id


def specify_phone_number_id(entry_id: str):
    """specifies the entry that should contains random phone numbers"""
    global phone_number_id
    phone_number_id = entry_id


def check_if_entry_is_name_or_id(entry_id: str):
    if entry_id == global_name_id:
        return random.choice(random_names)
    if entry_id == phone_number_id:
        return random.choice(random_phone_numbers)
    return False


def get_name_id():
    global global_name_id
    return global_name_id


def get_phone_id():
    global phone_number_id
    return phone_number_id

# if __name__ == '__fillChoices__':
#     fillChoices()
